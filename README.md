# Scan4Health 🥗📷

Scan4Health is a smart food health analysis web application that scans packaged food barcodes and provides nutritional insights, ingredient alerts, health score, rating, and consumption recommendations.

## Features
- Barcode scanning using camera (QuaggaJS)
- Manual barcode input support
- Real-time product data fetching using OpenFoodFacts API
- NLP-based ingredient analysis (keyword detection)
- Health scoring model (0–100)
- Rating system (Healthy / Moderately Healthy / Unhealthy)
- Auto dataset logging into CSV for testing validation
- Clean UI with progress bar and color-coded score

## Technologies Used
- Python
- Flask
- HTML, CSS, JavaScript
- OpenFoodFacts API
- QuaggaJS (barcode scanner)

## How to Run
1. Clone repository
2. Install dependencies:

```bash
pip install -r requirements.txt