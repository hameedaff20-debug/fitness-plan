import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")


def update_workout_plan(original_plan: str, user_feedback: str) -> str:
    """Use Gemini to update the workout plan based on user feedback."""
    prompt = f"""
You are a professional fitness trainer assistant.

Here's the original 7-day workout plan:
{original_plan}

User Feedback:
"{user_feedback}"

Based on the feedback, revise the relevant parts of the workout plan. Keep the format and rest of the plan unchanged if not needed.
"""
    try:
        if client is None:
            raise RuntimeError("GOOGLE_API_KEY is not set.")
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )
        return (response.text or "").strip()
    except Exception as e:
        return f"Error updating plan: {e}"
