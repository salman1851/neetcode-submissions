class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        time = [0]*len(pairs)
        for i, p in enumerate(pairs):
            time[i] = (target - p[0])/p[1]
        st = []
        for t in time:
            if not st:
                st.append(t)
            else:
                if not t <= st[-1]:
                    st.append(t)
        return len(st)        