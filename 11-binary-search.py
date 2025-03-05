import bisect
from typing import List

# ITERATION
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            mid_number = nums[mid_index]

            if target == mid_number:
                return mid_index
            elif target < mid_number:
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1
        return -1
    # TC - O(logn)
    # SC - O(1)

# RECURSION
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        left_index =  0
        right_index = len(nums) - 1
        return self.binary_search(left_index, right_index, nums, target)
    
    def binary_search(self, left_index, right_index, nums, target):
        if right_index < left_index:
            return -1
        
        mid_index = (left_index+right_index)//2
        mid_number = nums[mid_index]
        
        if target==mid_number:
            return mid_index
        elif target < mid_number:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1
            
        return self.binary_search(left_index, right_index, nums, target)
    
    # TC - O(logn)
    # SC - O(logn) -- Stack space
    

# BUILT IN function python
class Solution3:
    def search(self, nums, target):
        index = bisect.bisect_left(nums, target)
        if index < len(nums) and nums[index] == target:
            return index
        return -1
    
    # TC - O(logn)
    # SC - O(1)
            