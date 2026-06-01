# There is an O(1) solution, it involves indexing on value not on 


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        # target - number
        for num_pos in range(len(nums)):
            # {value: pos}
            num = nums[num_pos]
            x = target - num
            y = seen.get(x, None)
            print(f"{num_pos=}, {x=}, {y=}")
            if y is None:
                seen[num] = num_pos
                continue
            return [y, num_pos]
            
