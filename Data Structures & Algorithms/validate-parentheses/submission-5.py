class Solution:
    def isValid(self, s: str) -> bool:

        st = []
        brack = {")":"(", "}":"{", "]":"["}
        
        for i, o in enumerate(s):

            # append opening bracket to stack
            if o == "(" or o == "{" or o == "[": 
                st.append(o)
            
            # invalid if the top of the stack is not the mirror of the current character
            else:
                if st:
                    if st.pop() != brack[o]:
                        return False
                else:
                    return False

        # stack should be empty at the end
        if st:
            return False

        return True