import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")


def generate_nutrition_tip_with_flash(goal: str) -> str:
    """Generate a practical nutrition or recovery tip for the user's goal."""
    prompt = (
        f"Give one clear, helpful nutrition or recovery tip for someone focused on '{goal}'. "
        "The tip should be practical, friendly, and easy to understand."
    )
    try:
        if client is None:
            raise RuntimeError("GOOGLE_API_KEY is not set.")
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )
        return (response.text or "").strip()
    except Exception as e:
        return f"Error generating tip: {str(e)}"
