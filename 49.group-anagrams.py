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
# Solution 1: brute force
# For each
{
    97: ['eat', 'tea']
}

# @lc code=start
class Solution(object):
    def getASCII(self, str):
        result = 0
        for i in range(0, len(str)):
            result += ord(str[i])
        return result
    
    def isAnagrams(self, s, t):
        my_dict = {}

        if(len(t) != len(s)):
            return False

        for i in range(len(s)):
            if(my_dict.get(s[i]) is None):
                my_dict[s[i]] = 1
            else: 
                my_dict[s[i]] += 1

        for i in range(len(t)):
            if(my_dict.get(t[i]) is None):
                return False
            else:
                my_dict[t[i]] -= 1

        for index, value in enumerate(my_dict):
            if(my_dict[value] != 0):
                return False


        return True

    def groupAnagrams(self, strs):
        hash_table: dict[int, list[str]] = {} 
        n = len(strs)
        for i in range(0, n):
            total_ascii = self.getASCII(strs[i])
            if(hash_table.get(total_ascii) is None):
                hash_table[total_ascii] = [strs[i]]
            elif (self.isAnagrams(hash_table[total_ascii][0], strs[i])): 
                hash_table[total_ascii].append(strs[i])
            else:
                hash_table[total_ascii + i] = [strs[i]] ## alone

        grouped: list[list[str]] = list(hash_table.values())
        return grouped






        
        
# @lc code=end

# ✅ Đoạn để debug - viết test case ở đây
if __name__ == "__main__":
    sol = Solution()
    result = sol.groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"])
    print("Result:", result)
