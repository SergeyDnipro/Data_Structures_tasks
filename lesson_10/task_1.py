from typing import List

results_array = [7,6,4,3,1]

def max_profit(prices: List[int]) -> int:
    n = len(prices)
    max_profit = 0
    for buy_day in range(n - 1):
        for sell_day in range(buy_day + 1, n):
            profit = prices[buy_day] - prices[sell_day]
            if profit < 0 and abs(profit) > max_profit:
                max_profit = abs(profit)
    return max_profit

print(max_profit(results_array))