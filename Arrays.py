#1. Two Sum
def twoSum(self, nums: List[int], target: int) -> List[int]:
	seenAt = {}
	for i , num in enumerate(nums):
		s = target-num
		if s in seeAt:
			return [i, seenAt[s]]
		seenAt[num] = i

#26. Remove Duplicates from Sorted Array
def removeDuplicates(self, nums: List[int]) -> int:
	if not nums :return 0
	#Pythonic 
        # nums[:] = list(dict.fromkeys(nums)) #nums[:] to prevent creating a new list
        # return len(nums)

	#algorithmic
	for i in range(len(nums)-1,0,-1):
		if nums[i]==nums[i-1]:
			del nums[i]
	return len(nums)


	#Two pointers:
	# if not nums :return 0
	# i = 0
	# for j in range(1, len(nums)-1):
	# 	if nums[i] != nums[j]:
	# 		i+=1
	# 		nums[i] = nums[j]

#27. Remove Element
    def removeElement(self, nums: List[int], val: int) -> int:
	#Pythonic
        nums[:] = [num for num in nums if num != val]
        return len(nums)
	#algo
	i, n = 0,len(nums)
	while i<n:
		if nums[i] == val:
			nums[i] = nums[n-1]
			n-=1;
		else:
			i+=1
	
	return n


#35. Search Insert Position
def searchInsert(self, nums: List[int], target: int) -> int:
	#O(log n)
	left, right = 0, len(nums)-1
	mid = (right+left)//2
	while(left< right):
		if target<mid:
			right = mid
		elif target>mid:
			left = mid + 1
		else:
			return mid
		
		mid = (right+left)//2

	return mid

#53. Maximum Subarray
def maxSubArray(self, nums: List[int]) -> int:
#Kadanes
	maxi = s = nums[0]
	for num in range(nums[1:]):
		s = max(num, s+num)
		maxi = max(maxi, s)
	return maxi 
#66. Plus One

def plusOne(self, digits: List[int]) -> List[int]:
	r = 1
	for i in range(len(digits)-1,-1,-1):
		if  r != 0:
			digits[i] +=1
			if digits[i] == 10:
				digits[i] == 0
				r = 1
			else:
				r=0
				break
	if r == 1:
		return [1]+digits

	return digits

#88. Merge Sorted Array
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
	while m>0 and n>0:
		if nums1[m-1]>nums[n-1]:
			nums[m+n-1]  = nums[m-1]
			m-=1
		else:
			nums[m+n-1]  = nums[n-1]
			n-=1
	nums1[:n] = nums2[:n]
 
 
 
#108. Convert Sorted Array to Binary Search Tree
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

	def convert(left:int , right:int) ->TreeNode:
		if left>right:
			return None
		mid = (right+left)//2
		node  = TreeNode(nums[mid])
		node.left= convert(left, mid-1)
		node.right = convert(mid+1, right)
		return node

	return convert(0, len(nums)-1)

#121. Best Time to Buy and Sell Stock
def maxProfit(self, prices: List[int]) -> int:
	#Kadanes
	profit, buy_day = 0, prices[0]
	for price in prices[1:]:
		buy_day = min(buy_day, curr)
		profit = max(profit, price-buy_day) 

	return ans

#122. Best Time to Buy and Sell Stock II
def maxProfit(self, prices: List[int]) -> int:
	profit = 0
	for i, price in enumerate(prices[:-1]):
		if price< prices[i+1]:
			profit +=prices[i+1] + price

	return profit	
	

#136. Single Number
def singleNumber(self, nums: List[int]) -> int:
	hmap = defaultdict(int)
	for num in nums :
		hmap[num]+=1

	for key, val in hmap.items():
		if val == 1:
			return key

	#XOR
	# ans = 0
	# for num in nums :
	# 	ans ^=num
	# return num