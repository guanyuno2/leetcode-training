#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (64.59%)
# Likes:    18366
# Dislikes: 732
# Total Accepted:    2.9M
# Total Submissions: 4.5M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap_table = {}
        n = len(nums)

        # dem tan suat
        for i in range(len(nums)):
            if(hashmap_table.get(nums[i]) is None):
                hashmap_table[nums[i]] = 1
            else:
                hashmap_table[nums[i]] += 1

        # this is deep create array
        bucket = [[] for i in range(n + 1)]

        for key, value in hashmap_table.items():
            bucket[value].append(key)
    
        result = []
        
        for i in range(n, 0 , -1):
            for j in range(len(bucket[i])):
                if(len(result) == k): 
                    return result
                result.append(bucket[i][j])

        return result
        
# @lc code=end

# ✅ Đoạn để debug - viết test case ở đây
if __name__ == "__main__":
    sol = Solution()
    result = sol.topKFrequent([1,1,1,2,2,3], 2)
    print("Result:", result)