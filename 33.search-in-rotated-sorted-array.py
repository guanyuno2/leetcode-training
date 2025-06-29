#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (42.86%)
# Likes:    28175
# Dislikes: 1708
# Total Accepted:    3.6M
# Total Submissions: 8.5M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
# 
# Prior to being passed to your function, nums is possibly rotated at an
# unknown pivot index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
# and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4
# 
# Solution: Binary Search Tree
# Need to be 

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = (right + left) // 2
            if(nums[mid] == target):
                return mid
            
            # kiem tra 1/2 trai sorted
            if(nums[left] <= nums[mid]):
                # kiem tra 1/2 sorted trai
                if (nums[left] <= target < nums[mid]):
                    # target nằm trong khoảng này
                    right = mid - 1
                else: 
                    # target ko thuộc đoạn này => chắc chắn thuộc phải 1/2 phải
                    left = mid + 1
            else:
                if (nums[mid] < target <= nums[right]):
                    left = mid + 1
                else:
                    # target không thuộc đoạn này
                    right = mid - 1
                

        return -1
        
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    result = sol.search([1], 0)
    print("Result:", result)
