#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (66.65%)
# Likes:    13103
# Dislikes: 434
# Total Accepted:    4.9M
# Total Submissions: 7.3M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# 
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# Solution: using Hash map
# using for loop to store count each value appear in that string
# with the next string, we are check again if existed that character and minus 1
# then use another loop that hash map to check if any character had count > 0 then return false
# else return true
# Time: O(3n)
# Space: O(1), 26 English letter only

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        my_dict = {}
        for index, value in enumerate(s):
            if(my_dict.get(value) is None):
                my_dict[value] = 1
            else: 
                my_dict[value] = my_dict[value] + 1
        
        for index, value in enumerate(t):
            if(my_dict.get(value) is None):
                return False
            else:
                my_dict[value] = my_dict[value] - 1

        for index, value in enumerate(my_dict):
            if(my_dict[value] != 0):
                return False
            
        return True

        
        
# @lc code=end

# ✅ Đoạn để debug - viết test case ở đây
if __name__ == "__main__":
    sol = Solution()
    result = sol.isAnagram("ab", "a")
    print("Result:", result)