import requests

def get_product_by_barcode(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    try:
        response = requests.get(url, timeout=60)
        data = response.json()

        if data.get("status") == 1:
            product = data["product"]

            return {
                "product_name": product.get("product_name", "Unknown"),
                "ingredients_text": product.get("ingredients_text", "Not available"),
                "protein": product.get("nutriments", {}).get("proteins_100g", 0),
                "sugar": product.get("nutriments", {}).get("sugars_100g", 0),
                "fat": product.get("nutriments", {}).get("fat_100g", 0),
                "calories": product.get("nutriments", {}).get("energy-kcal_100g", 0),
                "additives_count": product.get("additives_n", 0)
            }

        return None

    except requests.exceptions.Timeout:
        print("❌ OpenFoodFacts API Timeout")
        return None

    except Exception as e:
        print("❌ API Error:", e)
        return None