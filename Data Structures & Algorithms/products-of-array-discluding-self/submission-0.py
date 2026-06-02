import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            #print(f"{i=}")
            # shallow copy
            prod_list = nums.copy()
            prod_list.pop(i)
            prod = math.prod(prod_list)
            #print(f"{prod_list=}")
            #print(f"{prod=}")
            out.append(prod)
        return out
