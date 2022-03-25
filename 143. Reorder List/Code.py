def cutinhalf(head):
    fast, slow = head.next, head
    if not fast:
        return None
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    if fast.next:
        slow=slow.next
    x = slow.next
    slow.next = None
    return x
def reverse(head):
    if not head or not head.next:
        return head
    p,c,n = head, head.next, head.next.next
    p.next = None
    while n:
        c.next = p
        p, c, n = c, n, n.next
    c.next = p
    return c
    

class Solution(object):
    def reorderList(self, head):
        h = cutinhalf(head)
        h = reverse(h)
        p = head
        while h:
            h2 = h.next
            h.next = p.next
            p.next = h
            p = p.next.next
            h = h2
        return head