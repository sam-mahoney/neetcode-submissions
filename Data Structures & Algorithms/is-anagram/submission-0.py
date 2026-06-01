class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # they will be the same length
        if len(s) != len(t):
            return False
        
        # capture both, sort, same
        x = "".join(sorted(s))
        y = "".join(sorted(t))
        if x == y:
            return True
        return False
