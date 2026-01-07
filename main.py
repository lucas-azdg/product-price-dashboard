import csv

# --- LEER CSV ---
products = []
with open("products.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = {
            "name": row["Product Name"].strip(),
            "price": float(row["Price"].strip())
        }
        products.append(product)

# --- MÉTRICAS ---
prices = [p["price"] for p in products]
total_products = len(products)
average_price = sum(prices) / total_products
most_expensive = max(products, key=lambda x: x["price"])
cheapest = min(products, key=lambda x: x["price"])

# --- DASHBOARD ---
def print_bar(label, value, scale=50):
    max_value = max(prices)
    bar_length = int(value / max_value * scale)
    bar = "█" * bar_length
    print(f"{label:15} | {bar} {value:.2f}")

print("\n=== PRODUCT PRICE DASHBOARD ===")
print(f"Total Products: {total_products}")
print(f"Average Price: {average_price:.2f}")
print(f"Most Expensive: {most_expensive['name']} ({most_expensive['price']:.2f})")
print(f"Cheapest: {cheapest['name']} ({cheapest['price']:.2f})\n")

print("Product Prices:")
for p in products:
    print_bar(p["name"], p["price"])





