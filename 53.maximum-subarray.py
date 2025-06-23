#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Medium (52.09%)
# Likes:    35835
# Dislikes: 1515
# Total Accepted:    5M
# Total Submissions: 9.7M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the subarray with the largest sum, and
# return its sum.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# 
# 
# Example 3:
# 
# 
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
# 
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
# 
#
# Solution 1: Brute force algorithm
# We have 2 loops which the second always less than equal then i
# Time: O(N^2)
# Space: O(1)
#
# Solution 2: using Dynamic Programming
# Loop each elements and compare between the current value and (previous sum + current value)
# If the current value is greater, then start new subarray sum here 
# Time: O(N)
# Space: O(1)


# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        temp_sum = max_sum = nums[0] # hold the first index of subarray
        for i in range(1, len(nums)):
            temp_sum = max(temp_sum + nums[i], nums[i])
            max_sum = max(temp_sum, max_sum)

        return max_sum
    



        
# @lc code=end

# ✅ Đoạn để debug - viết test case ở đây
if __name__ == "__main__":
    sol = Solution()
    result = sol.maxSubArray([1])
    print("Result:", result)
