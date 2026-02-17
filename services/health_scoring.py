def calculate_health_score(protein, sugar, fat, calories, additives_count):
    score = 100

    # Sugar penalty
    if sugar > 20:
        score -= 25
    elif sugar > 10:
        score -= 15
    elif sugar > 5:
        score -= 5

    # Fat penalty
    if fat > 20:
        score -= 20
    elif fat > 10:
        score -= 10

    # Calorie penalty
    if calories > 400:
        score -= 20
    elif calories > 250:
        score -= 10

    # Additives penalty
    score -= additives_count * 2

    # Protein bonus
    if protein > 10:
        score += 5

    # Keep score between 0 and 100
    score = max(0, min(score, 100))

    return score


def get_rating_and_recommendation(score):
    if score >= 80:
        return "✅ Healthy", "Good for regular consumption"
    elif score >= 50:
        return "⚠ Moderately Healthy", "Consume in moderation"
    else:
        return "❌ Unhealthy", "Avoid frequent consumption"