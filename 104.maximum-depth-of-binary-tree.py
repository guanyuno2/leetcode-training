#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (77.15%)
# Likes:    13618
# Dislikes: 268
# Total Accepted:    4.1M
# Total Submissions: 5.3M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return its maximum depth.
# 
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: root = [1,null,2]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -100 <= Node.val <= 100
# 
# 
# Solution: Recursive
# Time: O(n) // in the worst case we'll be literally all nodes
# Space: O(n) // each node we must have new instace of left and right

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# if empty tree: depth = 0
#
#
#


class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        
        # in the end of the leaf node, both bellow will be 0,0 and it's must plus 1
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1

       
        
        
# @lc code=end

