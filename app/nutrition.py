from app.gemini_flash_generator import generate_nutrition_tip_with_flash


def get_tailored_nutrition_tip(goal: str) -> str:
    """
    Wrapper for nutrition logic.
    """
    return generate_nutrition_tip_with_flash(goal)