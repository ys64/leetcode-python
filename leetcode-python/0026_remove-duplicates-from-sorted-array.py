from typing import List


class Solution:
    # 07/14/2020
    def removeDuplicates(self, nums: List[int]) -> int:
        f = 0  # dummy
        i = 0
        while i < len(nums):
            if i == 0:
                f = nums[0]
                i += 1
            else:
                if f == nums[i]:
                    nums.remove(f)
                else:
                    f = nums[i]
                    i += 1

        return len(nums)


s = Solution()
print(s.removeDuplicates([1, 2]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
