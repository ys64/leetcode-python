from typing import List


class Solution:
    # 07/20/2020
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = 0

        for i, n in enumerate(nums):
            if n == target:
                return i
            else:
                if n < target:
                    ans = i
                else:
                    return i

        return len(nums)


class Solution2:
    # 04/14/2021
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if target <= n:
                return i

        return len(nums)


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 7))
print(s.searchInsert([1, 3, 5, 6], 0))
print(s.searchInsert([1], 0))
