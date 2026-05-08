class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_list = []
        for s in strs:
            ana = {}
            for c in s:
                ana[c] = ana.get(c, 0) + 1
            ana_list.append(ana)

        ana_grp = {}
        for i, ana in enumerate(ana_list):
            curr_grp = "".join(f"{k}{v}" for k, v in dict(sorted(ana.items())).items())
            if curr_grp not in ana_grp:
                ana_grp[curr_grp] = [i]
            else:
                ana_grp[curr_grp].append(i)

        final_lst = []
        for k, v in ana_grp.items():
            final_lst.append([strs[i] for i in v])

        return final_lst