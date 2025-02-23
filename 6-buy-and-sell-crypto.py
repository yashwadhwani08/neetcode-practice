class Solution1:
    def maxProfit(self, prices: List[int]) -> int:        
        decreasing_prices = sorted(prices, reverse=True)
        if prices == decreasing_prices or len(prices)==1:
            return 0
        max_profit = 0
        buy_day, sell_day = 0,1

        while(buy_day < sell_day and sell_day < len(prices)):
            if prices[buy_day] > prices[sell_day]:
                buy_day = sell_day
            elif prices[buy_day] < prices[sell_day]:
                profit = prices[sell_day] - prices[buy_day]
                max_profit = max(max_profit, profit)    
            sell_day += 1
        return max_profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]
        
        for sell in prices:
            maxP = max(maxP, sell-minBuy)
            minBuy = min(minBuy, sell)
        return maxP
        
        