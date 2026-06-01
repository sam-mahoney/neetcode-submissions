class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        for num in nums:
            x = dups.get(num, 0)
            if x + 1 > 1:
                return True
            dups[num] = x + 1
        return False

