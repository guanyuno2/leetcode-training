#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (63.23%)
# Likes:    12937
# Dislikes: 1329
# Total Accepted:    5.2M
# Total Submissions: 8.2M
# Testcase Example:  '[1,2,3,1]'
#
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1]
# 
# Output: true
# 
# Explanation:
# 
# The element 1 occurs at the indices 0 and 3.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,4]
# 
# Output: false
# 
# Explanation:
# 
# All elements are distinct.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# 
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#


# solution: using hash map
# using loop for each element and count it into hash map
# if existed that elements before, then return true
# return false in finally
# Time: O(n)
# Space: O(n): In worst case, if every elements is distinct

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        my_dict = {}
        for index, value in enumerate(nums):
            if(my_dict.get(value) is None):
                my_dict[value] = 1
            else: 
               return True
        return False
            
           
           
        
# @lc code=end
# ✅ Đoạn để debug - viết test case ở đây
if __name__ == "__main__":
    sol = Solution()
    result = sol.containsDuplicate([2,7,11,15], 9)
    print("Result:", result)
