class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_found = {}
        for i, x in enumerate(nums):
            needed = target - x
            if needed in map_found:
                return [map_found[needed], i]
            map_found[x] = i