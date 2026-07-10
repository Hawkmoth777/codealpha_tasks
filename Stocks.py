STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 400.00,
    "AMZN": 175.00
}
portfolio = {}

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks to track:", ", ".join(STOCK_PRICES.keys()))
while True:
    symbol = input("\nEnter the stock ticker (or type 'done' to finish): ").upper()
    
    if symbol == 'DONE':
        break 
        
    if symbol not in STOCK_PRICES:
        print("Sorry, that stock is not in our database. Try one from the list.")
        continue
        
    try:
        quantity = float(input(f"How many shares of {symbol} do you own? "))
        
        if quantity < 0:
            print("Quantity cannot be negative. Please try again.")
            continue
        if symbol in portfolio:
            portfolio[symbol] += quantity
        else:
            portfolio[symbol] = quantity
            
    except ValueError:
        print("Invalid input! Please enter a valid number for the quantity.")

print("      PORTFOLIO SUMMARY      ")

total_investment = 0.0

for sym, qty in portfolio.items():
    price = STOCK_PRICES[sym]
    value = price * qty     
    total_investment += value
    print(f"{sym}: {qty} shares @ ${price:.2f} each = ${value:.2f}")

print("-" * 30)
print(f"TOTAL INVESTMENT VALUE: ${total_investment:.2f}")