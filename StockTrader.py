"""
Author: Kevin Van
Date: 12/02/2022

Stock trader algorithm that returns the best profit from one purchase and sale 
of stock. Input of an array of stock prices where indices are minutes into the trading day
Note: Not allowed to buy and sell on adjacent minutes.

Assumptions
    1. Market is open for at least 3 minutes (Compulsory one buy and one sell, not adjacent)
    2. Negative prices and negative profit is fine


Usage:
    Instantiate class with stock prices array and call method max_profit_trade() to receive the value of the max profit trade.
    See TestStockTrader.py
"""

class StockTrader:

    def __init__(self, stock_prices):
        if len(stock_prices) < 3: 
            raise Exception("Not enough prices to make trade")
        self.stock_prices = stock_prices


    """ 
    Iterates through stock prices O(n) and calculates profits w/r to the minimum buyable price before
    that time which is the previous minimum not adjacent. Max profit is updated
    """
    def max_profit_trade(self):
        max_profit = float("-inf")
        # Keeps minimum prices to calculate potential profits from
        min_price_buyable = self.stock_prices[0]
        min_price_seen = min(min_price_buyable, self.stock_prices[1])
        
        for i in range(2, len(self.stock_prices)):
            # Check best profit at current time and update if best overall
            sell_price = self.stock_prices[i]
            profit = sell_price - min_price_buyable
            max_profit = max(profit, max_profit)
            
            min_price_buyable = min(min_price_seen, min_price_buyable)
            min_price_seen = min(min_price_seen, sell_price)

        return max_profit





