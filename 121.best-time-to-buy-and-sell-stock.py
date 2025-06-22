#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (55.25%)
# Likes:    33348
# Dislikes: 1286
# Total Accepted:    6.5M
# Total Submissions: 11.7M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
# 
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# 
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.
# 
# 
# Example 1:
# 
# 
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you
# must buy before you sell.
# 
# 
# Example 2:
# 
# 
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit =
# 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
# 
# 
#

# Solution: Using for loop
# At Once time, you just choose 1 action: Buy / Sell
# If current value is Minimum, then buy it
# Recalculate if we buy current value is best profit, then store profit
# return latest profit
# if dont have any profit, then return 0
# Time: O(n)
# Space: O(1)

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        minimun_price = float('inf') # this is positive infinity
        profit = 0
        for index, value in enumerate(prices):
            if(value < minimun_price):
                minimun_price = value
            elif ((value - minimun_price) > profit):
                profit = value - minimun_price

        return profit
        
        
# @lc code=end

# ✅ Đoạn để debug - viết test case ở đây
if __name__ == "__main__":
    sol = Solution()
    result = sol.maxProfit([7,1,5,3,6,4])
    print("Result:", result)

