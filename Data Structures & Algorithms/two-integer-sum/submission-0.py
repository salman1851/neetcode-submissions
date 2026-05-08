class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map_.keys():
                return [map_[diff], i]
            map_[n] = map_.get(n, i)