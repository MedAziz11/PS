def inorderTraversal(self, root: TreeNode) -> List[int]:
	return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
	if q and p :
		return q.val == p.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
	return p is q
	 

def isSymmetric(self, root: TreeNode) -> bool:
	l, r = root.left, root.right
	def check(l, r: TreeNode)->bool:
		if l and r :
			return l.val==r.val and check(l.left, r.left) and check(l.right, r.right)
		return l is r

	return check(l,r)


def maxDepth(self, root: TreeNode) -> int:
	if not root : return 0
	l, r = maxDepth(root.left), maxDepth(root.right)
	if l>r:
		return l+1
	return r+1


def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def convert(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)
            return node
        
        return convert(0, len(nums) - 1)


def isBalanced(self, root: TreeNode) -> bool:
	def height(root:TreeNode)->int:
		if not root:
			return -1
		return max(height(root.left), height(root.right))+1

	if not root :return True
	return abs(height(root.left)-height(root.right))< 2 and isBalanced(root.left) and isBalanced(root.right)


def minDepth(self, root: TreeNode) -> int:
	if not root: return 0
	q = collections.deque([(root,1)])
	while q:
		curr, level = q.popleft()
		if not curr.left and not curr.right:
			return level
		q.append((curr.left, level+1))
		q.append((cuur.right, level+1))
		  
def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
	if not root: return False
	q = collections.deque([(root, targetSum-root.val)])
	while q:
		curr, curr_sum = q.popleft()
		if not curr.left and not curr.right:
			if curr_sum == 0:
				return True
		
		if curr.left:
			q.append((curr.left, curr_sum-curr.left.val))

		if curr.right:
			q.append((curr.right, curr_sum-curr.right.val))

		
	return False

def preorderTraversal(self, root: TreeNode) -> List[int]:
	return [root.val] + preoderTraversal(root.left) + preoderTraversal(root.right) if root else []


def preorderTraversal(self, root: TreeNode) -> List[int]:
	return preoderTraversal(root.left) + preoderTraversal(root.right) + [root.val]  if root else []

def invertTree(self, root: TreeNode) -> TreeNode:
	if root : 
		root.left = invertTree(root.right)
		root.right = invertTree(root.left)
	return root

	#bfs
	if not root: return root
	q = collections.deque([(root)])
	while q : 
		curr = q.popleft()
		if root:
			curr.left , curr.right = curr.right, curr.left
		
		q.append(curr.left)
		q.append(curr.right)

	return root

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
	while (root.val-q.val)*(root.val-p.val)>0:
		root = (root.left, root.right)[root.val<p.val] 
	return root

    
def binaryTreePaths(self, root: TreeNode) -> List[str]:
	if not root : return []
	if not root.left and not root.right: return [str(root.val)]
	
	res = [str(root.val)+"->"+path for path in binarySearchPaths(root.left)]
	res + = [str(root.val)+ "->"+path for path in binarySearchPaths(root.right)]
	return res