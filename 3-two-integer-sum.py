class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
            return []
            
            # O(n^2) Time complexity, O(1) - space (no extra space)
            
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, num in enumerate(nums):
            indices[num] = index
            
        for index, num in enumerate(nums):
            diff =  target-num
            if diff in indices and indices[diff] != index:
                if index < indices[diff]:
                    return [index, indices[diff]]
                elif index > indices[diff]:
                    return [indices[diff], index]
            return []
            
            # O(n) Time complexity (for creating dictionary), O(n)-Dictionary space
            
# URL - https://neetcode.io/problems/two-integer-sum