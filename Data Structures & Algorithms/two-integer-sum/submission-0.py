class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, x in enumerate(nums):
            needed = target - x
            if needed in map:
                return [map[needed], i]
            map[x] = i