#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (36.93%)
# Likes:    42187
# Dislikes: 2053
# Total Accepted:    7.6M
# Total Submissions: 20.5M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without duplicate
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
# Solution: Sliding Window
# Time: O(n)
# Space: O(k)

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        hash_map = {} # where key is character and value is index
        result = 0
        n = len(s)
        for i in range(n):
            while hash_map.get(s[right]) is not None:
                del hash_map[s[left]]
                left += 1
            
            hash_map[s[right]] = right
            if((right - left) + 1 > result):
                result = (right - left) + 1
            right += 1
        return result
        
# @lc code=end

# ✅ Đoạn để debug - viết test case ở đây
if __name__ == "__main__":
    sol = Solution()
    result = sol.lengthOfLongestSubstring("dvdf")
    print("Result:", result)