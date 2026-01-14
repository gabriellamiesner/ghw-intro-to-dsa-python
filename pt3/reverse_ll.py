 def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head 
        prev = None

        while curr: 
            nxt = curr.next 
            curr.next = prev 
            prev = curr
            curr = nxt 
        return prev
