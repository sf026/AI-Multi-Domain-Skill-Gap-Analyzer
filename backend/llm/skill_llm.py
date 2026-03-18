from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def extract_skills_llm(text):

    prompt = f"""
    Extract all professional skills from this text.
    Return only comma separated skills.

    TEXT:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    skills = response.choices[0].message.content

    skills_list = [s.strip() for s in skills.split(",")]

    return skills_list