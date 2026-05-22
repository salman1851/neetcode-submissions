class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda a,b:a+b,
            "-": lambda a,b:a-b,
            "*": lambda a,b:a*b,
            "/": lambda a,b:int(a/b),
        }
        st = []
        for i, o in enumerate(tokens):
            if o not in ops:
                st.append(int(o))
            else:
                b = st.pop()
                a = st.pop()
                st.append(ops[o](a,b))
        return st[0]        