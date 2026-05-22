class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        st = []
        for i, o in enumerate(temperatures):
            while st and o > st[-1][1]: 
                (ind, elem) = st.pop()
                result[ind] = i-ind
            st.append((i,o))
        return result