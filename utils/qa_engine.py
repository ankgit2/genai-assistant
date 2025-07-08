# utils/qa_engine.py

import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2025-01-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")


def ask_question(document_text, user_question):
    prompt = f"""
You are a document analysis assistant.

Answer the user's question based ONLY on the following document:

--- BEGIN DOCUMENT ---
{document_text[:4000]}
--- END DOCUMENT ---

Your task:
1. Give a direct answer.
2. Add a short justification with reference to where in the document it came from. For example: "As stated in paragraph 3", or "Refer to page 2".

Question:
{user_question}
"""

    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that always uses document content and never guesses."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip(), "Answer justified using document content."


def generate_challenges(document_text):
    prompt = f"""Based on the following document, generate 3 logic-based or comprehension-focused questions.
Do not provide answers — only the questions.

Document:
{document_text[:2000]}
"""

    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You are a quiz question generator."},
            {"role": "user", "content": prompt}
        ]
    )

    quiz_text = response.choices[0].message.content.strip()
    questions = quiz_text.split("\n")
    challenges = []

    for q in questions:
        q = q.strip("-•1234567890. ").strip()
        if q:
            def dummy_eval(ans):
                return True, "Answer received (evaluation not automated)."
            challenges.append({"question": q, "evaluate": dummy_eval})

    return challenges
