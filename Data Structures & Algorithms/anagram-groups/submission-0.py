class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes = {}
        for string in strs:
            hashed_string = hash("".join(sorted(string)))
            exists = hashes.get(hashed_string, None)
            if exists is None:
                hashes[hashed_string] = [string]
            else:
                hashes[hashed_string] = exists + [string]
        return list(hashes.values())
