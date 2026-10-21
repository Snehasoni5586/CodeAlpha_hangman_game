# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker

print("=" * 45)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 45)

# Stock prices (sample prices in INR)
stock_prices = {
    "TCS": 3500,
    "INFY": 1800,
    "RELIANCE": 1400,
    "WIPRO": 500,
    "HDFC": 1700
}

portfolio = {}
total_investment = 0

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock:12} Rs. {price:,.2f}")

print("\nEnter your stock investments")
print("-" * 45)

while True:
    stock = input(
        "\nEnter stock name (or DONE to finish): "
    ).strip().upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock! Please choose from the list.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    print(f"{quantity} shares of {stock} added successfully!")

print("\n" + "=" * 45)
print("             PORTFOLIO REPORT")
print("=" * 45)

if not portfolio:
    print("No stocks added to your portfolio.")
else:
    print(f"{'STOCK':<12}{'QTY':>6}{'PRICE':>12}{'VALUE':>15}")
    print("-" * 45)

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = quantity * price
        total_investment += value

        print(
            f"{stock:<12}{quantity:>6}"
            f"{price:>12,.2f}{value:>15,.2f}"
        )

    print("-" * 45)
    print(f"Total Portfolio Value: Rs. {total_investment:,.2f}")

print("=" * 45)
print("     Thank you for using the tracker!")
print("=" * 45)