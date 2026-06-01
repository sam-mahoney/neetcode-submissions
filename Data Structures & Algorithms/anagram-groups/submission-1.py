from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            _id = "".join(sorted(string))
            # defaultdict, we don't have to do None check 
            groups[_id].append(string)
        return list(groups.values())
