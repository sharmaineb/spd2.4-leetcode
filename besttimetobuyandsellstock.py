"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

# initialize min_price and max_profit 
# iterate through the array of prices, updating them as we go
# update min_price
# update max_prift
# return the max_profit

class Solution:
    def maxProfit(self, prices):
        # check if the prices array is empty | return 0 because we can't make profit
        if not prices:
            return 0
        
        # initialize min_price to the first price in the array
        min_price = prices[0]

        # initialize max_profit to 0
        max_profit = 0

        # iterate through each price in the prices array
        for price in prices:
            # update min_price to be the minimum of the current price and the min_price so far
            min_price = min(min_price, price)

            # update max_profit to be the maximum of the current profit and the max_profit at the moment
            max_profit = max(max_profit, price - min_price)
        
        # return the max profit achieved
        return max_profit
    
sol = Solution()

prices1 = [7,1,5,3,6,4]
print(sol.maxProfit(prices1))