stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 130,
    "MSFT": 300
}

portfolio = {}

print("Enter your stock holdings (type 'done' to finish):")

while True:
    stock_name = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock_name == 'DONE':
        break
    if stock_name not in stock_prices:
        print("Stock not found in price list.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock_name} shares: "))
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

total_value = 0
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares x ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

save = input("Do you want to save the result to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares x ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print("Portfolio saved to 'portfolio_summary.txt'")
