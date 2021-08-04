from collections import *
from typing import *


class Solution:

    #79. Word Search
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(r:int, c:int, i:int):

            if i == len(word): return True
            if ( r<0 or c<0 or 
                r>=ROWS or c>=COLS or
               (r, c) in visited or
               word[i] != board[r][c] ):
                return False
            
            visited.add((r, c))
            res = (dfs(r + 1, c, i+1) or
                  dfs(r - 1, c, i+1) or
                  dfs(r, c + 1, i+1) or
                  dfs(r, c - 1, i+1) )
            visited.remove((r, c))

            return res
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):return True
                
        return False
    
    
    #784. Letter Case Permutation
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        
        def backtracking(i: int, ch:str):
            if i== len(s): ans.append(ch); return
            if s[i].isalpha():
                backtracking(i+1, ch+s[i].lower())
             
            backtracking(i+1, ch+s[i].upper())
           

        backtracking(0, "")


        return ans
    
    #78. Subsets
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def backtracking(i:int, subset: List[int]):
            if i == len(nums): ans.append(subset); return
            
            backtracking(i+1, subset + [nums[i]])
            backtracking(i+1, subset)
            
            
        backtracking(0, [])
        return ans
    
    #46. Permutations
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans  = []
        def backtrack(curr: List[int], possibilities: List[int]):
            if not possibilities: ans.append(curr); return
            
            for j, num in enumerate(possibilities):
                
                backtrack(curr+[num], possibilities[:j]+possibilities[j+1:] )
        
        backtrack([], nums)
        return ans
    
    #77. Combinations
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []                             
        def backtrack(curr: List[int]= [], start: int=1)-> None :
            if len(curr)== k: ans.append(curr); return
            for num in range(start, n+1):
                backtrack(curr+[num], num+1)
                
                
        backtrack()
        
        return ans
                