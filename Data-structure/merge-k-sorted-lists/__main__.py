"""
URL: https://leetcode.com/problems/merge-k-sorted-lists/

Description:
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """


# Testing:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


a = ListNode(1)
a2 = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
d2 = ListNode(4)
e = ListNode(5)
f = ListNode(6)

a.next = d
d.next = e

a2.next = c
c.next = d2

b.next = f

user_input = [
    a, a2, b
]
for node in user_input:
    print(node.val, node.next.val)
