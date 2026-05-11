class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # better computational expenditure

        s = sorted(set(nums)) # convert input into a set
        max_len = curr_len = 1
        for i in range(1,len(s)): # iterate from second till the last element
            if s[i] - s[i-1] == 1: # if the diff b/w curr and prev is unity
                curr_len += 1 # it's a valid sequence
                max_len = max(curr_len, max_len)
            else: # if the diff b/w curr and prev is greater than unity
                curr_len = 1 # it's not a valid sequence, reset the curr_len
        return max_len if s else 0