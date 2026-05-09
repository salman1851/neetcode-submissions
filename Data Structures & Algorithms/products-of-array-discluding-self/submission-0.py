import math
import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prf = [1]*len(nums)
        psf = [1]*len(nums)
        for i in range(len(nums)):
            prf[i] = math.prod(nums[:i])
            psf[i] = math.prod(nums[i:])
        psf = psf[1:]+[1] # left shift the array by 1
        return list(np.multiply(prf,psf))