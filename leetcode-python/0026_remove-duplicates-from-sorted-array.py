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


class Solution2:
    # 04/14/2021
    def removeDuplicates(self, nums: List[int]) -> int:
        # num is equal to or smaller than -10^4
        current_num = -(10 ** 5)
        current_index = 0

        while len(nums) != current_index:
            if nums[current_index] == current_num:
                nums.remove(current_num)
            else:
                current_num = nums[current_index]
                current_index += 1

        return len(nums)


s = Solution()
print(s.removeDuplicates([1, 2]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
