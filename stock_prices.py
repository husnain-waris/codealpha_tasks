stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2750,
    "MSFT": 300
}

portfolio = {}

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not in our list.")
        continue
    quantity = input(f"Enter quantity for {stock}: ")
    if quantity.isdigit():
        portfolio[stock] = int(quantity)
    else:
        print("Please enter a valid number.")
        continue

total_value = 0

for stock in portfolio:
    price = stock_prices[stock]
    qty = portfolio[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} × ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

save = input("Do you want to save the result? (yes/no): ").lower()
if save == "yes":
    file_type = input("Choose file type (.txt or .csv): ").lower()
    if file_type == ".txt":
        f = open("portfolio.txt", "w")
        for stock in portfolio:
            qty = portfolio[stock]
            price = stock_prices[stock]
            f.write(f"{stock}: {qty} × ${price} = ${qty * price}\n")
        f.write(f"\nTotal Investment Value: ${total_value}")
        f.close()
    elif file_type == ".csv":
        f = open("portfolio.csv", "w")
        f.write("Stock,Quantity,Price,Total\n")
        for stock in portfolio:
            qty = portfolio[stock]
            price = stock_prices[stock]
            f.write(f"{stock},{qty},{price},{qty * price}\n")
        f.write(f"Total Investment,,,{total_value}")
        f.close()
    print("Portfolio saved successfully.")
