
import csv

# Stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250
}

print("=== Stock Portfolio Tracker ===")

total_investment = 0

# Get quantity from user
portfolio = {}

for stock, price in stocks.items():
    quantity = int(input(f"Enter quantity of {stock}: "))
    investment = price * quantity

    portfolio[stock] = {
        "price": price,
        "quantity": quantity,
        "investment": investment
    }2

    total_investment += investment

# Display portfolio
print("\n--- Your Portfolio ---")

for stock, details in portfolio.items():
    print(
        f"{stock}: Price = ${details['price']}, "
        f"Quantity = {details['quantity']}, "
        f"Investment = ${details['investment']}"
    )

print(f"\nTotal Investment: ${total_investment}")

# Save portfolio to TXT file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Report\n")
    file.write("----------------------\n")

    for stock, details in portfolio.items():
        file.write(
            f"{stock}: Price=${details['price']}, "
            f"Quantity={details['quantity']}, "
            f"Investment=${details['investment']}\n"
        )

    file.write(f"\nTotal Investment: ${total_investment}\n")

# Save portfolio to CSV file
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Price", "Quantity", "Investment"])

    for stock, details in portfolio.items():
        writer.writerow([
            stock,
            details["price"],
            details["quantity"],
            details["investment"]
        ])

    writer.writerow(["", "", "Total", total_investment])

print("\nPortfolio saved to portfolio.txt and portfolio.csv")