#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (70.95%)
# Likes:    20613
# Dislikes: 695
# Total Accepted:    3.8M
# Total Submissions: 5.4M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# 
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 
# Explanation:
# 
# 
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form
# each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to
# form each other.
# 
# 
# 
# Example 2:
# 
# 
# Input: strs = [""]
# 
# Output: [[""]]
# 
# 
# Example 3:
# 
# 
# Input: strs = ["a"]
# 
# Output: [["a"]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# 
# 
#
# Solution 1: 
# For each
# Time: O(n * k log k): mỗi chuỗi cần O(k log k) để sort
#   Duyệt và thao tác dict/list: O(1) trung bình
# Space: - O(n * k): cần lưu `n` chuỗi (trong dict và kết quả)
#   O(k): bộ nhớ tạm cho việc sort từng chuỗi
#   


# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        hash_table = {}
        for i in range(len(strs)):
            sorted_string = ''.join(sorted(strs[i]))
            if(hash_table.get(sorted_string) is None):
                hash_table[sorted_string] = [strs[i]]
            else:
                hash_table[sorted_string].append(strs[i])
        result = []
        for index, key in enumerate(hash_table):
            result.append(hash_table[key])
        return result





        
        
# @lc code=end

# ✅ Đoạn để debug - viết test case ở đây
if __name__ == "__main__":
    sol = Solution()
    result = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print("Result:", result)
