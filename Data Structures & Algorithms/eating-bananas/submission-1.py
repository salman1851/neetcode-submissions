import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        left, right = 1, k
        min_k = k
        while left <= right:
            k = (left + right) // 2
            hrs = 0
            for p in piles:
                hrs += math.ceil(float(p) / k)
            if hrs <= h:
                min_k = min(min_k, k)
                right = k - 1
            else:
                left = k + 1
        return min_k