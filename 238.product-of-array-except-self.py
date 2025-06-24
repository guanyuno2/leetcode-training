#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (67.79%)
# Likes:    24267
# Dislikes: 1569
# Total Accepted:    3.7M
# Total Submissions: 5.4M
# Testcase Example:  '[1,2,3,4]'
#
# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
# 
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# You must write an algorithm that runs in O(n) time and without using the
# division operation.
# 
# 
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit
# integer.
# 
# 
# 
# Follow up: Can you solve the problem in O(1) extra space complexity? (The
# output array does not count as extra space for space complexity analysis.)
# 
# Solution: Prefix/suffix
# using 2 loops to calculate prefix and suffix each elements

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)

        prefix_array = [1] * n
        suffix_array = [1] * n

        next_left = 1
        for i in range(n):
            prefix_array[i] = next_left
            next_left *= nums[i]

        next_right = 1
        for i in reversed(range(n)):
            suffix_array[i] = next_right
            next_right *= nums[i]
        
        result = [1] * n
        for i in range(n):
            result[i] = prefix_array[i] * suffix_array[i]
        return result


       
                    

        
        
# @lc code=end

# ✅ Đoạn để debug - viết test case ở đây
if __name__ == "__main__":
    sol = Solution()
    result = sol.productExceptSelf([-1,1,0,-3,3])
    print("Result:", result)
