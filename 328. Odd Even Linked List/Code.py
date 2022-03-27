class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        o=head
        e=head.next
        
        while e and e.next:
            x = e.next
            e.next = e.next.next
            x.next = o.next
            o.next = x
            e = e.next
            o = o.next
        return head
    