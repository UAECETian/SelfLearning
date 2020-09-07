from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[num] = index
        return [prevMap[diff], index]


ann = Solution()
test = ann.twoSum([2, 7, 11, 15, 12, 13, 11], 22)
print(test)