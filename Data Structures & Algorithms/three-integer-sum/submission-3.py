class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        for i, o in enumerate(nums):
            start = i+1
            end = len(nums)-1
            while end-start >= 1:
                if nums[i]+nums[start]+nums[end] > 0:
                    end -= 1
                elif nums[i]+nums[start]+nums[end] < 0:
                    start += 1
                else:
                    sort_trip = sorted([nums[i],nums[start],nums[end]])
                    if sort_trip not in triplets: triplets.append(sort_trip)
                    start += 1
        return triplets