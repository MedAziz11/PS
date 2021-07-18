from typing import *
from collections import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    
    
    #704. Binary Search
    def search(self, nums: List[int], target: int) -> int:
        #Time O(log(N)), Space O(1) 
        l, r = 0, len(nums)-1
        while l<= r:
            mid =(l+r)//2
            
            if nums[mid] == target:
                return mid
            
            if target>nums[mid]:
                l = mid+1
            elif target< nums[mid]:
                r = mid-1
 
        return -1
    
    #744. Find Smallest Letter Greater Than Target
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #Time O(log(N)), Space O(1) 
        l, r = 0 , len(letters)
        while l<r:
            mid = (l+r)//2
            if letters[mid]<=target:
                l = mid+1
            else: r = mid
                
        return letters[l % len(letters)]
                
    
    #852. Peak Index in a Mountain Array
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #Time O(log(N)), Space O(1) 
        l, r = 0, len(arr)-1
        while (l<=r):
            mid = (l+r)//2
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            if arr[mid-1]>arr[mid]>arr[mid+1]:
                r = mid-1
            else:
                l = mid+1
    
    
    #637. Average of Levels in Binary Tree
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q = deque([root])
        res = []
        
        while q:
            s, n= 0, len(q)
            for _ in range(n):
                node = q.popleft()
                s+=node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
            res.append(s/n)
            
        return res
    
    
    #111. Minimum Depth of Binary Tree
    def minDepth(self, root: TreeNode) -> int:
        #BFS
        if not root :return 0
        q = deque([root, 1])
        while q:
            curr, lvl = q.popleft()
            if curr:
                if not curr.left and not curr.right:
                    return lvl
                q.append((curr.left, lvl+1))
                q.append((curr.right, lvl+1))

        #DFS
        # if not root :return 0
        # if not root.left or not root.right: return max(self.minDepth(root.left), self.minDepth(root.right))+1
        # return min(self.minDepth(root.left), self.minDepth(root.right))+1




    #100. Same Tree
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:	
        if q and p:
            return q.val == p.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return q is p



    #112. Path Sum
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root : return False
        q = deque([(root, targetSum-root.val)])
        while q:
            curr, r = q.popleft()
            if curr:
                if not curr.left and not curr.right:
                    if not r : return True
                if curr.left : q.append((curr.left, r-curr.left.val))
                if curr.right : q.append((curr.right, r-curr.right.val))

        return False

    #543. Diameter of Binary Tree
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        def depth(root: TreeNode)-> int:
            if not root:  return 0
            l = depth(root.left)
            r = depth(root.right)
            self.diameter = max(self.diameter, l+r)
            return max(l, r)+1

        depth(root)
        return self.diameter

    #617. Merge Two Binary Trees
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        #using tree 1
#         if not root1: return root2
#         if not root2: return root1
#         root1.val+= root2.val
#         root1.left = self.mergeTrees(root1.left, root2.left)
#         root1.right = self.mergeTrees(root1.right, root2.right)
        
#         return root1

    # creating new tree
        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        return root1 or root2

    #104. Maximum Depth of Binary Tree
    def maxDepth(self, root: TreeNode) -> int:
        if not root : return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l, r)+1

    #235. Lowest Common Ancestor of a Binary Search Tree
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        	
        if p.val<root.val>q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val>root.val<q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root