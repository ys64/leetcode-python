from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            for ii, nn in enumerate(nums[i + 1 :]):
                if n + nn == target:
                    # print(i, (i + 1) + ii)
                    return [i, (i + 1) + ii]

        return []  # cannot find


s = Solution()
s.twoSum([2, 7, 11, 15], 9)
