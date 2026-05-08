from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        cnt_sort = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
        return [x for x, y in cnt_sort[:k]]