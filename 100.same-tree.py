#
# @lc app=leetcode id=100 lang=python
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (65.16%)
# Likes:    12269
# Dislikes: 269
# Total Accepted:    2.9M
# Total Submissions: 4.4M
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given the roots of two binary trees p and q, write a function to check if
# they are the same or not.
# 
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.
# 
# 
# Example 1:
# 
# 
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: p = [1,2], q = [1,null,2]
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in both trees is in the range [0, 100].
# -10^4 <= Node.val <= 10^4
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):

        # Nếu cả hai đều rỗng → giống nhau
        if not p and not q:
            return True
        
        # Nếu một cái rỗng, một cái không → khác nhau
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
       
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        
# @lc code=end

