def stock_portfolio():
    # Hardcoded dictionary defining stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 400,
        "AMZN": 175
    }

    print("Available Stocks and Prices per share:")
    for stock, price in stock_prices.items():
        print(f"- {stock}: ${price}")

    total_investment = 0
    portfolio = {}

    while True:
        stock_name = input("\nEnter stock symbol to buy (or type 'done' to finish): ").upper()
        if stock_name == 'DONE':
            break
        
        if stock_name not in stock_prices:
            print("Stock not found in price list. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
        except ValueError:
            print("Please enter a valid number for quantity.")
            continue

        cost = stock_prices[stock_name] * quantity
        total_investment += cost
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f"Added {quantity} shares of {stock_name} for ${cost}")

    print("\n--- Portfolio Summary ---")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares (Value: ${qty * stock_prices[stock]})")
    print(f"Total Investment Value: ${total_investment}")

    # Optional: Save result to a text file
    with open("portfolio_summary.txt", "w") as f:
        f.write(f"Total Investment Value: ${total_investment}\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares\n")
    print("\nPortfolio summary saved to 'portfolio_summary.txt'.")

if __name__ == "__main__":
    stock_portfolio()