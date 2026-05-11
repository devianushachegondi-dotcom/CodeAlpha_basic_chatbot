# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300
}
total_value = 0
n = int(input("How many different stocks do you own? "))
for i in range(n):
    stock_name = input("Enter stock name (AAPL,TSLA,GOOGL,MSFT): ").upper()
    quantity = int(input("Enter quantity: "))
    if stock_name in stock_prices:
        investment = stock_prices[stock_name]*quantity
        total_value += investment
        print(f"{stock_name}: ₹{investment}")
    else:
        print("Stock not found. Skipping.")
print("Total portfolio value: ₹", total_value)