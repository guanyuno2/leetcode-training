#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (42.32%)
# Likes:    25917
# Dislikes: 1885
# Total Accepted:    6.2M
# Total Submissions: 14.5M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# 
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# 
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: s = "([])"
# 
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

# Solution: Using hash map to predefine all characters and Stack to manager order of characters
# if next characters is one of Symmetric character, then pop stack, and double check with that value
# Time: O(n)
# Space: O(k), which k belongs ... 


# @lc code=start
class Solution(object):
    def isValid(self, s):
        my_dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for index, value in enumerate(s):
            if(my_dict.get(value) is None):
                stack.append(value) # open
            else: 
                if(len(stack) == 0):
                    return False
                character = stack.pop() # open
                if(my_dict.get(value) != character):
                    return False

        return len(stack) == 0

        
# @lc code=end

# ✅ Đoạn để debug - viết test case ở đây
if __name__ == "__main__":
    sol = Solution()
    result = sol.isValid("([])}")
    print("Result:", result)
