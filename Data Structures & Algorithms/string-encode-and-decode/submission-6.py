class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_ = ""
        for curr_word in strs:
            curr_len = len(curr_word)
            enc_ += f"{curr_len}#{curr_word}"
        return enc_

    def decode(self, s: str) -> List[str]:
        word_len = 0
        word_len_ch = []
        dec_ = []
        for i, ch in enumerate(s):
            if word_len != 0:
                word_len -= 1
                continue
            if ch.isdigit():
                word_len_ch += ch
            if ch == "#":
                word_len = int("".join(word_len_ch))
                dec_.append(s[i+1:i+1+word_len])
                word_len_ch = []
        return dec_