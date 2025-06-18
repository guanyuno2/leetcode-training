/*
 * @lc app=leetcode id=121 lang=javascript
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
    let minPrice = 1000000000
    let maxProfit = 0
    for (var i = 0; i < prices.length; i++) {
        if (prices[i] < minPrice) {
            // if price today is smaller, then not buy, just hold min
            minPrice = prices[i]
        }
        else {
            // re calculate if we sell it today
            let profit = prices[i] - minPrice
            if (profit > maxProfit)
                maxProfit = profit
        }
    }
    return maxProfit
};
// @lc code=end
