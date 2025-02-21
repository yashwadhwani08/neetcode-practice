class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            if target-i in nums:
                return [nums.index(i), nums.index(target-i)]
            
            # O(n^2) Time complexity, O(1) - space (no extra space)
            
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, num in enumerate(nums):
            indices[num] = index
            
        for index, num in enumerate(nums):
            diff =  target-num
            if diff in indices and indices[diff] != index:
                return [index, indices[diff]]
            
            # O(n) Time complexity (for creating dictionary), O(n)-Dictionary space
            
# URL - https://neetcode.io/problems/two-integer-sum