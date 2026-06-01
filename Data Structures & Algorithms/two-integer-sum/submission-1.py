class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # left left everytime it's incorrect
        # we need to return in array
        d = {}
        # arr_pos: number
        # populate dict
        pos = []
        for arr_pos in range(len(nums)):
            d[arr_pos] = nums[arr_pos]
        
        # can we do it with two sets? 

        for k,v in d.items():
            d2 = {x:y for x,y in d.items() if x !=k}
            for x,y in d2.items(): 
                pos2 = x
                lol = v + y
                if lol == target:
                    return [k, pos2]
            