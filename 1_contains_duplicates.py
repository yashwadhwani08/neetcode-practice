class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in nums:
           nums_set.add(i)
        if len(nums_set) == len(nums):
            return False
        return True
            
# URL - https://neetcode.io/problems/duplicate-integer