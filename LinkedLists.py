#21. Merge Two Sorted Lists
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
	curr = root = ListNode()
	while l1 and l2:
		if l1.val>l2.val:
			curr.next = curr = ListNode(l2.val)
			l2 = l2.next
		else:
			curr.next = curr = ListNode(l1.val)
			l1 = l1.next

		
	curr.next = l1 or l2
	return root.next

#83. Remove Duplicates from Sorted List
def deleteDuplicates(self, head: ListNode) -> ListNode:
	curr = head
	while curr :
		while curr.next and curr.val == curr.next.val:
			curr.next = curr.next.next
		
		curr= curr.next
	return head

#141. Linked List Cycle
def hasCycle(self, head: ListNode) -> bool:
	#O(N) , O(N)
	curr = head
	visited= set()
	while curr:
		if curr in visited:
			return True
		visited.add(curr)
		curr = curr.next

	return False
	#O(N) ,O(1)	
	
	#fast =  slow = head 
        #while fast  and fast.next :
        #    fast = fast.next.next
        #    slow = slow.next
        #    if fast == slow: return True

        #return False

#160. Intersection of Two Linked Lists
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
	#O(N+M) , O(1)
	currA , currB = headA, headB
	while currA != currB:
		currA = currA.next if currA.next else headB
		currB = currB.next if currB.next else headA 

	#O(N), O(N)
	#curr, hashset = head, set()
	#while curr :
	#	hashset.add(curr)
	#	curr = curr.next
	
	#curr = headB
	#while curr:
	#	if curr in hashset:
	#		return True
	#	curr = curr.next
	

#203. Remove Linked List Elements
def removeElements(self, head: ListNode, val: int) -> ListNode:
	
	while head.val == val:
		head = head.next

	curr = head
	while curr.next:
		if curr.next.val = val:
			curr.next = curr.next.next

		curr = curr.next

	return head


#206. Reverse Linked List
def reverseList(self, head: ListNode) -> ListNode:
	prev , curr = None, head
	while curr:
		tmp = curr.next
		curr.next = prev
		prev = curr
		curr = tmp

	return prev

#234. Palindrome Linked List
def isPalindrome(self, head: ListNode) -> bool:
	fast = slow = head
	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next
	
	prev = None
	while slow:
		tmp = slow.next
		slow.next = prev
		prev = slow
		slow = tmp
	
	curr = head
	while prev:
		if prev.val != curr.val:
			return False
		
		curr = curr.next
		prev = prev.next
	
	return False

#237. Delete Node in a Linked List
def deleteNode(self, node:ListNode)->None:
	node.val = node.next.val
	node.next = node.next.next

#876. Middle of the Linked List
def middleNode(self, head: ListNode) -> ListNode:
	fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow

#1290. Convert Binary Number in a Linked List to Integer
def getDecimalValue(self, head: ListNode) -> int:
	num, curr = head.val , head
	while curr.next:
		num += num<<1 | curr.next.val
		curr = curr.next
	return num