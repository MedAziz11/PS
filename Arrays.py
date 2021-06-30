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
