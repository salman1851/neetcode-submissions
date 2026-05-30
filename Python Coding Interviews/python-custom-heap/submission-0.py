import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    nums_heap = []
    for n in nums:
        pair = (-n, n)
        heapq.heappush(nums_heap, pair)
    nums_heap_rev = []
    while nums_heap:
        nums_heap_rev.append(heapq.heappop(nums_heap)[1])
    return nums_heap_rev


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
