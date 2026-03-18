import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# ----------------------------
# Load ESCO Occupations
# ----------------------------

occ_df = pd.read_csv(r"C:\Users\sfshi\OneDrive\Desktop\AI_SKILL_GAP_ANALYZER\backend\modules\data\occupations_en.csv")

OCCUPATIONS = occ_df["preferredLabel"].dropna().str.lower().tolist()

occupation_embeddings = model.encode(OCCUPATIONS, convert_to_tensor=True)


# ----------------------------
# Load Occupation-Skill Mapping
# ----------------------------

relation_df = pd.read_csv(r"C:\Users\sfshi\OneDrive\Desktop\AI_SKILL_GAP_ANALYZER\backend\modules\data\occupationSkillRelations_en.csv")

occupation_skill_map = {}

for _, row in relation_df.iterrows():

    occ = row["occupationLabel"].lower()
    skill = row["skillLabel"].lower()

    if occ not in occupation_skill_map:
        occupation_skill_map[occ] = []

    occupation_skill_map[occ].append(skill)


# ----------------------------
# Detect Profession
# ----------------------------

def detect_profession(text):

    text_embedding = model.encode(text, convert_to_tensor=True)

    scores = util.cos_sim(text_embedding, occupation_embeddings)[0]

    best_idx = scores.argmax()

    return OCCUPATIONS[best_idx]


# ----------------------------
# Get Expected Skills
# ----------------------------

def get_expected_skills(profession):

    return occupation_skill_map.get(profession, [])