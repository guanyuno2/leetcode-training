#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (79.23%)
# Likes:    23081
# Dislikes: 533
# Total Accepted:    5.3M
# Total Submissions: 6.7M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: [2,1]
# 
# 
# Example 3:
# 
# 
# Input: head = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
# 
# 
# 
# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head

        while current:
           next_node = current.next
           current.next = prev

           prev = current
           current = next_node

        return prev

        
# @lc code=end

# ✅ Đoạn để debug - viết test case ở đây
if __name__ == "__main__":
    sol = Solution()
    result = sol.containsDuplicate([2,7,11,15], 9)
    print("Result:", result)
