import re

# Keywords for detection
SUGAR_KEYWORDS = ["sugar", "glucose", "fructose", "syrup", "sucrose"]
PALM_OIL_KEYWORDS = ["palm oil", "palmolein"]
PRESERVATIVE_KEYWORDS = ["preservative", "sodium benzoate", "potassium sorbate"]
ADDITIVE_PATTERN = r"\bE\d{3,4}\b"   # matches E100, E211 etc.


def analyze_ingredients(ingredients_text: str, sugar_value: float, additives_count: int):
    """
    Analyze ingredients text and nutrition values to generate health alerts.
    Returns a list of alert strings.
    """

    alerts = []

    if not ingredients_text:
        return ["Ingredients information not available"]

    text = ingredients_text.lower()

    # 1. High sugar (from nutrition)
    if sugar_value is not None and sugar_value > 10:
        alerts.append("⚠ High sugar content")

    # 2. Sugar in ingredients list
    for word in SUGAR_KEYWORDS:
        if word in text:
            alerts.append("⚠ Contains added sugar")
            break

    # 3. Palm oil detection
    for word in PALM_OIL_KEYWORDS:
        if word in text:
            alerts.append("⚠ Contains palm oil")
            break

    # 4. Preservatives detection
    for word in PRESERVATIVE_KEYWORDS:
        if word in text:
            alerts.append("⚠ Contains preservatives")
            break

    # 5. Additives (E-numbers)
    e_numbers = re.findall(ADDITIVE_PATTERN, ingredients_text.upper())
    if e_numbers or additives_count > 0:
        alerts.append(f"⚠ Contains additives ({additives_count})")

    if not alerts:
        alerts.append("✅ No major harmful ingredients detected")

    return alerts
