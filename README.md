# Luna AI - Trading Bot

This is a simulation of the **Luna AI** trading bot designed to interact with the **pump.fun** website. The bot uses a simple trading strategy that includes buy/sell actions based on simulated market data.

## Features

- **Simulated Market Data**: The bot fetches simulated prices for trading.
- **Automated Trading**: The bot buys and sells assets based on predefined settings.
- **Profit & Stop-Loss**: The bot automatically stops trading when the profit target or stop-loss is hit.

## How to Use

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/luna-ai-trading-bot.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Edit the `config.json` file to configure the bot settings (starting balance, profit target, etc.).

4. Run the trading bot:
    ```bash
    python trading_bot.py
    ```

## Configuration

You can modify the trading parameters in the `config.json` file:
- **starting_balance**: Set the initial balance.
- **trade_amount**: Define the number of assets to buy/sell in each trade.
- **profit_target**: The balance at which the bot will stop trading.
- **stop_loss**: The balance at which the bot will stop trading to avoid further losses.

## Example Output

```bash
Starting trading bot with $10000 balance.
Current market price: $2334.12
Buying 1 units at $2334.12
Balance after purchase: $6665.88
Selling 1 units at $2389.34
Balance after sale: $10055.22
Profit target reached!
