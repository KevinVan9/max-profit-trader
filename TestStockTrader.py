"""
Author: Kevin Van
Date: 12/02/2022

Testing of StockTrader.py
"""
from StockTrader import StockTrader


'''
Test cases and expected output added here. Match cases and output with corresponding index
'''
TEST_CASES = [
    [10, 7, 5, 12, 11, 9],
    [30, 28, 26, 17, 11, 3, 23, 8, 12, 11, 15, 6, 16, 14], 
    [1,2,1], # Minimum number of prices
    [3,2,1], # Negative profit
    [-1,-3,-2,-1], # Negative prices
    [2,5,5,1,0],
    [4,2,7,1,6,4],
    [3,2,1,2],
    [1,2],
    [1],
    [] #Empty
]

EXPECTED = [
    6,
    13,
    0,  # 1 - 1 = 0
    -2, # 1 - 3 = -2
    2, # -1 - (-3)
    3, # 4 - 1
    4, # 6 - 2
    0, # 2 - 2
    None,
    None,
    None
]


'''
Testing code running trader's max profit trade and checking output
'''
failed=list()
for answer, stock_prices in zip(EXPECTED, TEST_CASES):
    try:
        trader = StockTrader(stock_prices)
        profit = trader.max_profit_trade()
        if answer != profit:
            failed.append(f'{stock_prices} Profit={profit}, Max={answer}')
    except Exception as e:
        print("Exception:", e)
        print("Case:", stock_prices)
        if answer is not None:
            failed.append(stock_prices)

if failed:
    print("Failed tests")
    for f in failed: print(f)
else:
    print("\nPassed!")
