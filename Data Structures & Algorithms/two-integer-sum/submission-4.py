class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in hash_map:
                return [hash_map[needed], i]
            hash_map[num] = i