class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # corrected by Claude for O(1) lookup

        num_set = set(nums)
        max_len = 0

        for n in num_set:
            if n - 1 not in num_set:  # only start counting at sequence heads
                cur_len = 1
                while n + cur_len in num_set:
                    cur_len += 1
                max_len = max(max_len, cur_len)

        return max_len