import csv
import os

FILE_NAME = "testing_log.csv"

def log_product_data(product_data, score, rating):
    file_exists = os.path.isfile(FILE_NAME)

    product_name = product_data["product_name"].strip().lower()

    # --- Step 1: Read existing product names ---
    existing_products = set()

    if file_exists:
        with open(FILE_NAME, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # skip header

            for row in reader:
                if len(row) > 0:
                    existing_products.add(row[0].strip().lower())

    # --- Step 2: If already exists, skip writing ---
    if product_name in existing_products:
        print(f"⚠ Product '{product_data['product_name']}' already exists. Skipping log.")
        return

    # --- Step 3: Write new product ---
    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write header if file doesn't exist
        if not file_exists:
            writer.writerow([
                "Product Name",
                "Sugar",
                "Fat",
                "Calories",
                "Additives",
                "Health Score",
                "Rating"
            ])

        writer.writerow([
            product_data["product_name"],
            product_data["sugar"],
            product_data["fat"],
            product_data["calories"],
            product_data["additives_count"],
            score,
            rating
        ])

    print(f"✅ Logged new product: {product_data['product_name']}")