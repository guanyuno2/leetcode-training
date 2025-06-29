#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (66.86%)
# Likes:    23480
# Dislikes: 2305
# Total Accepted:    5.3M
# Total Submissions: 8M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# You are given the heads of two sorted linked lists list1 and list2.
# 
# Merge the two lists into one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
# 
# Return the head of the merged linked list.
# 
# 
# Example 1:
# 
# 
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# 
# 
# Example 2:
# 
# 
# Input: list1 = [], list2 = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: list1 = [], list2 = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
# 
# Time: O(n+m)
# Space: O(1): Không tạo thêm node mới

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if(list1.val < list2.val):
                current.next = list1
                list1 = list1.next
                current = current.next
            else:
                current.next = list2
                list2 = list2.next
                current = current.next

        current.next = list1 if list1 else list2

        return dummy.next

def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print("Result:", result)

        
# @lc code=end
# ✅ Đoạn để debug - viết test case ở đây
if __name__ == "__main__":
    sol = Solution()
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 5])
    merged = sol.mergeTwoLists(l1, l2)
    print("Result:", merged)

