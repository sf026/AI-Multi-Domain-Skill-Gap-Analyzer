import spacy
import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Load sentence transformer
model = SentenceTransformer("all-MiniLM-L6-v2")

# -------------------------------
# Load ESCO Skills Dataset
# -------------------------------

skills_df = pd.read_csv(r"C:\Users\sfshi\OneDrive\Desktop\AI_SKILL_GAP_ANALYZER\backend\modules\data\skills_en.csv")

# Extract skill names
SKILL_DB = skills_df["preferredLabel"].dropna().str.lower().tolist()

print(f"Loaded {len(SKILL_DB)} skills from ESCO dataset")

# Generate embeddings for all ESCO skills
skill_embeddings = model.encode(SKILL_DB, convert_to_tensor=True)

# -------------------------------
# Stopwords / noise phrases
# -------------------------------

STOPWORDS = [
    "job title",
    "job summary",
    "career growth",
    "work environment",
    "their clients",
    "the job",
    "key responsibilities"
]

# -------------------------------
# Skill Extraction Function
# -------------------------------

def extract_skills(text):

    doc = nlp(text)

    phrases = []

    # Extract noun phrases
    for chunk in doc.noun_chunks:

        phrase = chunk.text.lower().strip()

        if phrase in STOPWORDS:
            continue

        if len(phrase.split()) > 4:
            continue

        if len(phrase) < 3:
            continue

        phrases.append(phrase)

    if not phrases:
        return []

    # Convert phrases to embeddings
    phrase_embeddings = model.encode(phrases, convert_to_tensor=True)

    matched_skills = []

    # Compare phrase embeddings with ESCO skill embeddings
    for i, emb in enumerate(phrase_embeddings):

        scores = util.cos_sim(emb, skill_embeddings)[0]

        best_idx = scores.argmax()

        if scores[best_idx] > 0.55:
            matched_skills.append(SKILL_DB[best_idx])

    # Remove duplicates
    return list(set(matched_skills))