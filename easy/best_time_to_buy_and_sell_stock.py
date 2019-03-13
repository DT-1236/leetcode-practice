class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Takes a list of numbers and returns the highest difference from left to right"""
        if len(prices) < 2:
            return 0
        best = 0
        local_min = prices[0]
        local_max = prices[0]
        for price in prices[1:]:
            if price < local_min:
                best = max(local_max - local_min, best)
                local_min = local_max = price
            else:
                local_max = max(local_max, price)
        return max(local_max - local_min, best)