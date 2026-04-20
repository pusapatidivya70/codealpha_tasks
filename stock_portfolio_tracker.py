# CodeAlpha_StockPortfolioTracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 170,
    "MSFT": 320
}

portfolio = {}

print("=== Stock Portfolio Tracker ===")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break

    if stock not in stocks:
        print("Stock not found. Available:", list(stocks.keys()))
        continue

    try:
        qty = int(input("Enter quantity: "))
    except:
        print("Invalid quantity")
        continue

    if stock in portfolio:
        portfolio[stock] += qty
    else:
        portfolio[stock] = qty

# Calculation
total = 0

print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    price = stocks[stock]
    value = price * qty
    total += value
    print(stock, "Qty:", qty, "| Price:", price, "| Value:", value)

print("\nTotal Investment Value:", total)

# Optional file save
save = input("\nSave result to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio Summary\n\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares @ {stocks[stock]}\n")
        f.write(f"\nTotal Investment: {total}\n")

    print("Saved to portfolio.txt")