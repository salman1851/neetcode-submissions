class Solution:
    def encode(self, strs: List[str]) -> str:
        # join() batches all concatenation into one O(n) operation
        return "".join(f"{len(w)}#{w}" for w in strs)

    def decode(self, s: str) -> List[str]:
        dec_ = []
        i = 0
        while i < len(s):
            # find the '#' delimiter, parse length in one shot
            j = s.index("#", i)
            word_len = int(s[i:j])
            dec_.append(s[j+1 : j+1+word_len])
            i = j + 1 + word_len  # jump directly to next encoded word
        return dec_