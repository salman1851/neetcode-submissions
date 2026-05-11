class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = sorted(list(set(nums))) # convert input into a set
        s.append(0) # add a dummy value at the end
        seq = [] # create an empty list for holding temporary sequence
        lar_seq = [] # create an empty list for holding max length sequences
        for i in range(len(s)-1): # iterate till the second last element
            seq.append(s[i])
            if len(seq) > len(lar_seq): # if the current sequence is greater than the largest sequence
                lar_seq = seq # update the largest sequence to be the current sequence
            if s[i+1] - s[i] != 1: # if the next element is greater by 1
                seq = [] # it's no longer a valid sequence

        return len(lar_seq)