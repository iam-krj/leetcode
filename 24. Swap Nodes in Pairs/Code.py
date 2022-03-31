class Solution(object):
    def swapPairs(self, head):  
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        x = head.next.next
        head.next.next = head
        newhead = head.next           
        head.next = self.swapPairs(x)
        return newhead 
            # p = p.next
            # p.next = p
            # p = x
            
        return head