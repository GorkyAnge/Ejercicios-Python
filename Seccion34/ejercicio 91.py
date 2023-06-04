def max_profit(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Maximum profit:", profit)
