from collections import *
from typing import *

class Solution:
    #217. Contains Duplicate
    def containsDuplicate(self, nums: List[int]) -> bool:
        #O(1) time, O(1) space
        return len(set(nums)) != len(nums)
    
    #268. Missing Number
    def missingNumber(self, nums: List[int]) -> int:
        #O(N) time, O(1) space
        #Using XOR
        ans = len(nums)
        for i, num in enumerate(nums):
            ans ^= i ^ num
            
        return ans
    
    #448. Find All Numbers Disappeared in an Array
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #O(N) time, O(N) space
        #using diffenrence between 2 sets which is really fast in python
        # return list(set(range(1, len(nums)+1)) - set(nums))
        
        #O(N) time, O(1) space
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
                
        return [i + 1 for i, num in enumerate(nums) if num > 0]
    
    #136. Single Number
    def singleNumber(self, nums: List[int]) -> int:
        #O(N) time, O(N) space
        #using hashmap that contains each number's occurence
        c= defaultdict(int)
        for num in nums:
            c[num] +=1
            
        for key, value in c.items():
            if 1 == value:
                return key
            
    #70. Climbing Stairs
    def climbStairs(self, n: int, memo:Dict[int, int] ={1:1, 2:2} ) -> int:
        #O(N) time, O(N) space
        #Memoization
        if n not in memo: 
            memo[n] = self.climbStairs(n-1, memo)+ self.climbStairs(n-2, memo)
        return memo[n]
    

    #121. Best Time to Buy and Sell Stock
    def maxProfit(self, prices: List[int]) -> int:
        #O(N) time, O(1) space
        #Kadane's Algorithm
        maxi, curr =0, prices[0]
        for price in prices[1:]:
            curr = min(curr, price)
            maxi = max(maxi, price-curr)

        return maxi

    #53. Maximum Subarray
    def maxSubArray(self, nums: List[int]) -> int:
        #O(N) time, O(1) space
        #Kadane's Algorithm
        
        maxi , s = nums[0],nums[0]
        
        for num in nums[1:]:
            s = max(s+num, num)
            maxi = max(maxi, s)
            
        return maxi
    
    #todo devide and conquer Solution
    
#303. Range Sum Query - Immutable
class NumArray:
    #using a memoization to keep track of sum of a range
    def __init__(self, nums: List[int]):
        self.memo = {}
        for i , num in enumerate(nums):
            self.memo[i]= self.memo.get(i-1, 0) + num
        

    def sumRange(self, left: int, right: int) -> int:
        return self.memo[right] - self.memo.get(left-1, 0)
    
    
    


