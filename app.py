from flask import Flask, render_template, request
from services.openfoodfacts_service import get_product_by_barcode
from services.ingredient_analysis import analyze_ingredients
from services.health_scoring import calculate_health_score, get_rating_and_recommendation
from services.logger import log_product_data


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        barcode = request.form.get("barcode")

        product_data = get_product_by_barcode(barcode)

        if not product_data:
            return render_template("error.html")

        alerts = analyze_ingredients(
            product_data["ingredients_text"],
            product_data["sugar"],
            product_data["additives_count"]
        )

        score = calculate_health_score(
            product_data["protein"],
            product_data["sugar"],
            product_data["fat"],
            product_data["calories"],
            product_data["additives_count"]
        )

        rating, recommendation = get_rating_and_recommendation(score)
        log_product_data(product_data, score, rating)

        return render_template(
            "result.html",
            product=product_data,
            alerts=alerts,
            health_score=score,
            rating=rating,
            recommendation=recommendation
        )

    # GET request case
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
