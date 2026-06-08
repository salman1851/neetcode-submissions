class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            if nums[i] == val:
                for k in range(i,j):
                    nums[k] = nums[k+1]
                j = j - 1
                i = i - 1
            i = i + 1           
        return i