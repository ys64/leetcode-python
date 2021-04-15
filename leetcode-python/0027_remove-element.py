from typing import List


class Solution:
    # 07/15/2020
    def removeElement(self, nums: List[int], val: int) -> int:
        ### This works, but elements which are equal to val
        ### need to be removed from nums.
        # count = 0

        # for n in nums:
        #     if n == val:
        #         count += 1

        # return len(nums) - count

        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(val)
            else:
                i += 1

        print(nums)
        return len(nums)


class Solution2:
    # 04/14/2021
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i != len(nums):
            if nums[i] == val:
                nums.remove(val)
            else:
                i += 1

        return len(nums)


s = Solution()
print(s.removeElement([3, 2, 2, 3], 3))
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
