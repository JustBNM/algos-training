class Solution:
    def maxProfit(self, prices) -> int:
        min_price = 10**5
        max_diff = 0
        for price in prices:
            min_price = min(min_price, price)
            diff = price - min_price
            max_diff = max(max_diff, diff)
        return max_diff