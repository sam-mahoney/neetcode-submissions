class Solution:
    # out of band
    # give the decoder meta data

    # take each string, and encode it into bytes or something
    # prepend a length byte
    # ascii
    def encode(self, strs: List[str]) -> str:
        data = ""
        sep = "#"
        for string in strs:
            length = len(string)
            rep = f"{length}{sep}{string}"
            # print(f"ENCODE => {rep=}")
            data = data + rep
        # print(f"ENCODE => {data=}")
        return data

    def decode(self, s: str) -> List[str]:
        print(f"DECODE => {s=}")
        data = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            size = int(s[i:j])
            start = j+1 
            end = start + size
            data.append(s[start:end])
            i = end

        return data
