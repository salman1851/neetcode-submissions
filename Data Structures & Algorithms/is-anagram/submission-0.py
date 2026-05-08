class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = {}
        d_t = {}
        for s in list(s):
            d_s[s] = d_s.get(s, 0) + 1
        for t in list(t):
            d_t[t] = d_t.get(t, 0) + 1
        return d_s == d_t