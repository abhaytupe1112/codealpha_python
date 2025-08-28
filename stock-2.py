# Stock Portfolio Tracker

def stock_portfolio():
    # Step 1: Hardcoded stock prices (dictionary)
    stock_prices = {
        "aapl": 180,
        "tsla": 250,
        "msft": 320,
        "googl": 140,
        "amzn": 135
    }

    portfolio = {}  # To store user input
    total_investment = 0

    print("Welcome to Stock Portfolio Tracker")
    print("Available stocks and prices:", stock_prices)

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").lower()

        if stock == "done":
            break
        if stock not in stock_prices:
            print("Stock not available. Please choose from:", list(stock_prices.keys()))
            continue

        try:
            qty = int(input(f"Enter quantity of {stock.upper()}: "))
            portfolio[stock] = portfolio.get(stock, 0) + qty
        except ValueError:
            print("Please enter a valid number.")

    # Step 2: Calculate total investment
    print("\nYour Portfolio:")
    for stock, qty in portfolio.items():
        value = qty * stock_prices[stock]
        total_investment += value
        print(f"{stock.upper()} - {qty} shares = ${value}")

    print("\nTotal Investment Value = $", total_investment)

    # Step 3: Save result to file
    choice = input("Do you want to save results to a file? (yes/no): ").lower()
    if choice == "yes":
        file_type = input("Enter file type (txt/csv): ").lower()
        if file_type == "txt":
            with open("portfolio.txt", "w") as f:
                f.write("Stock Portfolio Summary\n")
                for stock, qty in portfolio.items():
                    f.write(f"{stock.upper()} - {qty} shares = ${qty * stock_prices[stock]}\n")
                f.write(f"\nTotal Investment Value = ${total_investment}")
            print("Saved to portfolio.txt")
        elif file_type == "csv":
            with open("portfolio.csv", "w") as f:
                f.write("Stock,Quantity,Value\n")
                for stock, qty in portfolio.items():
                    f.write(f"{stock.upper()},{qty},{qty * stock_prices[stock]}\n")
                f.write(f"Total,,{total_investment}")
            print("Saved to portfolio.csv")
        else:
            print("Invalid file type. Skipping save.")

# Run the program
stock_portfolio()
