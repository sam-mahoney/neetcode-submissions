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
        # get int
        # capture next n chars
        # ...
        data = []
        while True:
            if not s:
                break
            split = s.split("#", maxsplit=1)
            size = int(split[0])
            s = split[-1]
            data.append(s[:size])
            s = s[size:]
            # print(f"DECODE => {size=}")
            # print(f"DECODE => {s=}")
            # print(f"DECODE => {data=}")

        return data
