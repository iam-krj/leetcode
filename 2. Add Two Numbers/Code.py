# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        ans = p = ListNode()
        while l1 and l2:
            k = l1.val+ l2.val + carry
            p.next = ListNode(k%10)
            carry = k//10
            p, l1, l2= p.next, l1.next, l2.next
        if l2:
            l1 = l2
        while l1:
            k = l1.val + carry
            p.next = ListNode(k%10)
            carry = k//10
            p, l1 = p.next, l1.next
        if carry:
            p.next = ListNode(carry)
        return ans.next
            