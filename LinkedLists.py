def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
	root = curr = ListNode()
	while l1 and l2:
		if l1.val<l2val:
			curr.next=curr=ListNode(l1.val)
			l1 = l1.next
		else:
			curr.next=curr=ListNode(l1.val)
			l2 = l2.next
		
	
	curr.next = l1 or l2
	return root.next


def deleteDuplicates(self, head: ListNode) -> ListNode:
	curr = head
	while curr:
		while curr.curr and curr.next.val == curr.val:
			curr.next = curr.next.next

		curr = curr.next

	return head


def hasCycle(self, head: ListNode) -> bool:
        curr , i= head, 0
        hash_map = {}
        while curr:
        
            if curr in hash_map:
                return True
            
            hash_map[curr] = i
            i+=1
            curr = curr.next 
            
        return False


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
         currA, currB = headA, headB
         while currA != currB:
             currA = currA.next if currA else headB
             currB = currB.next if currB else headA
            
         return currA
 
