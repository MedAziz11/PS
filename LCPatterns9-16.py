from collections import *
from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    #338. Counting Bits
    def countBits(self, n: int) -> List[int]:
        #O(n) Time, O(n) Space
        dp = [0] * (n+1)
        msb = 1
        for i in range(1, n+1):
            if msb * 2 == i:
                msb = i   
            dp[i] = 1+ dp[i-msb]
            
        return dp
    
    #141. Linked List Cycle
    
    #Fast Slow Pointer Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #O(n) Time, O(1) Space
        fast =  slow = head 
        while fast  and fast.next :
            fast = fast.next.next
            slow = slow.next
            if fast == slow: return True

        return False
    
    #using a set Solution
    def hasCycle(self, head: ListNode) -> bool:
        #O(n) Time, O(n) Space
        curr = head
        visited= set()
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next

        return False
    
    #876. Middle of the Linked List
    def middleNode(self, head: ListNode) -> ListNode:
        #O(n/2) Time, O(1) Space
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow
    
    #234. Palindrome Linked List
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        
        #getting the middle of the LinkedList
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        tail = None
        #Reverse the Linked List from the middle
        while slow:
            tmp = slow.next
            slow.next= tail
            tail = slow
            slow = tmp
        
        curr = head
        while tail:
            if tail.val != curr.val:
                return False
            curr = curr.next
            tail = tail.next
            
        return True  
        
    
    #203. Remove Linked List Elements
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        #O(n) Time, O(1) Space
        while head and head.val == val:
                head = head.next 
                
        curr = head
        while curr:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            
            curr = curr.next
            
        return head
    
    
    #83. Remove Duplicates from Sorted List
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #O(n) Time, O(1) Space
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
                
            cur = cur.next
                
        return head
    
    #206. Reverse Linked List
    def reverseList(self, head: ListNode) -> ListNode:
        #O(n) Time, O(1) Space
        curr = head
        prev = None
        while curr:
            tmp =  curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        return prev
    
    
    
    #21. Merge Two Sorted Lists
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #O(n+m) Time, O(n+m) Space
        cur = root = ListNode()
    
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = cur = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = cur = ListNode(l2.val)
                l2 = l2.next

        cur.next = l1 or l2
        return root.next
