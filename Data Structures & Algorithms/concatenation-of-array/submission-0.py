class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numel = len(nums)
        ans = [0]*2*numel
        for i in range(numel):
            ans[i] = nums[i]
            ans[i + numel] = nums[i]
        return ans