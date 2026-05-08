from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ana_grp = {}
        for i, s in enumerate(strs):
            key = "".join(f"{k}{v}" for k, v in sorted(Counter(s).items()))
            ana_grp.setdefault(key, []).append(s)  # store string directly, not index

        return list(ana_grp.values())