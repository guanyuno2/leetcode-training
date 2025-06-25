#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (50.99%)
# Likes:    10440
# Dislikes: 8551
# Total Accepted:    4.3M
# Total Submissions: 8.4M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
# 
# Given a string s, return true if it is a palindrome, or false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# 
# 
# Example 2:
# 
# 
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a
# palindrome.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
# 
# 
# Solution: Using 2-pointer
# Time: 0(n) Duyệt từ hai đầu mảng, mỗi ký tự được kiểm tra tối đa 1 lần.
# Space: O(1)



# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        n = len(s)
        left = 0 # index left
        right = n - 1 # index right
        while(left < right):
            currentLeft = s[left]
            currentRight = s[right]

            if not currentLeft.isalnum():
                left += 1
                continue
            if not currentRight.isalnum():
                right -= 1
                continue

            if(currentLeft.lower() != currentRight.lower()):
                return False
            
            left += 1
            right -= 1
            
            #make sure both left and right

        return True
        
# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    result = sol.isPalindrome("    ")
    print("Result:", result)
