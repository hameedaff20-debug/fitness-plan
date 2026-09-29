import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


def generate_workout_gemini(user_data: dict[str, str]) -> str:
	goal = user_data.get("goal", "general fitness")
	intensity = user_data.get("intensity", "moderate")
	prompt = (
		f"Create a practical workout plan for someone whose fitness goal is '{goal}' "
		f"at '{intensity}' intensity. Include exercises, sets, reps, and brief safety guidance."
	)
	try:
		if client is None:
			raise RuntimeError("GOOGLE_API_KEY is not set.")
		response = client.models.generate_content(
			model="gemini-3.5-flash",
			contents=prompt,
		)
		return (response.text or "").strip()
	except Exception as error:
		return f"Error generating workout plan: {error}"
