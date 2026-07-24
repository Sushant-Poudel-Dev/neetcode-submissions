class Solution:
    def maxProfit(self, prices: List[int]) -> int:     
        
        bestBuyValue = prices[0]
        profit = 0
        for price in prices:
            if price < bestBuyValue:
                bestBuyValue = price
            currentProfit = price - bestBuyValue
            if currentProfit > profit:
                profit = currentProfit
        return profit
