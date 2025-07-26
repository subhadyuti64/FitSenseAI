import os
import google.generativeai as genai


def get_style_tips(label: str) -> str:
    """Generate brief style advice using Gemini Flash."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY environment variable not set")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
    prompt = f"Give me concise fashion advice for a {label} outfit."
    response = model.generate_content(prompt)
    return response.text.strip()
