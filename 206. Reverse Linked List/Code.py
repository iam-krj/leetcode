# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        p, c, n = head, head.next, head.next.next
        p.next = None
        while n:
            c.next = p
            p =c
            c= n
            n=n.next
        c.next = p
        return c