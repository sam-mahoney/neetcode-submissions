class Solution:
    # out of band
    # give the decoder meta data
    def encode(self, strs: List[str]) -> str:
        data = ""
        sep = "#"
        for string in strs:
            length = len(string)
            rep = f"{length}{sep}{string}"
            data = data + rep
        return data

    def decode(self, s: str) -> List[str]:
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
