import time
import random
import json

# Load configuration settings from a config file
def load_config():
    with open('config.json') as f:
        return json.load(f)

# Simulate market data
def get_market_data():
    # Simulated random market price for the trading pair
    return random.uniform(1000, 5000)  # Random price between $1000 and $5000

# Simulate buying an asset
def buy_asset(amount, price):
    print(f"Buying {amount} units at ${price:.2f}")
    time.sleep(1)  # Simulate time delay for the trade
    return amount * price  # Return the total cost of the buy

# Simulate selling an asset
def sell_asset(amount, price):
    print(f"Selling {amount} units at ${price:.2f}")
    time.sleep(1)  # Simulate time delay for the trade
    return amount * price  # Return the total revenue from the sale

# Simulate trading strategy
def execute_trade():
    config = load_config()
    balance = config['starting_balance']
    amount_to_trade = config['trade_amount']
    profit_target = config['profit_target']
    stop_loss = config['stop_loss']

    print(f"Starting trading bot with ${balance} balance.")
    
    while balance > 0:
        market_price = get_market_data()
        print(f"Current market price: ${market_price:.2f}")
        
        # Buy action
        if balance >= market_price * amount_to_trade:
            total_spent = buy_asset(amount_to_trade, market_price)
            balance -= total_spent
            print(f"Balance after purchase: ${balance:.2f}")
            
            # Simulate a market fluctuation
            market_price += random.uniform(-50, 50)  # Price goes up or down
            
            # Sell action
            total_revenue = sell_asset(amount_to_trade, market_price)
            balance += total_revenue
            print(f"Balance after sale: ${balance:.2f}")
            
            # Check if the trade was profitable
            if balance >= profit_target:
                print("Profit target reached!")
                break
            elif balance <= stop_loss:
                print("Stop-loss reached, exiting trade.")
                break

        else:
            print("Not enough balance to make a trade.")
            break
        
        time.sleep(2)  # Wait before next trade

# Run the bot
if __name__ == "__main__":
    execute_trade()
