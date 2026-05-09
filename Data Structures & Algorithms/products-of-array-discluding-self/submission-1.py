class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res_prf = [1]*len(nums)
        res_suf = [1]*len(nums)
        res_fin = [1]*len(nums)
        for i in range(1,len(nums)):
            res_prf[i] = res_prf[i-1]*nums[i-1]
        suff = 1
        for i in range(len(nums)-2,-1,-1):
            res_suf[i] = res_suf[i+1]*nums[i+1]
        for i in range(len(nums)):
            res_fin[i] = res_prf[i]*res_suf[i]    
        return res_fin