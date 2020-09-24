from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        if len(nums3) % 2 != 0:
            return nums3[len(nums3) // 2]
        else:
            return (nums3[len(nums3) // 2] + nums3[len(nums3) // 2 - 1]) / 2


temp = Solution()

list = temp.findMedianSortedArrays([1,2,3,4,4,4],[4,5,6,7])
print(list)



