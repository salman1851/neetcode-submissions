class Solution:

    def is_number(self, n):
        try:
            n = int(n)
            return True
        except:
            return False

    def calPoints(self, operations: List[str]) -> int:
        st = []
        for o in operations:
            if self.is_number(o): st.append(int(o))
            elif o == "+": st.append(int(st[-1]) + int(st[-2]))
            elif o == "C": st.pop()
            elif o == "D": st.append(2*st[-1])
        return sum(st)