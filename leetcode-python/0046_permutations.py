from typing import List


class Solution:
    # 6/15/2021
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        result = []
        for n in nums:
            nums_excludes_n = [nn for nn in nums if nn != n]
            sub_permute = self.permute(nums_excludes_n)

            for i in range(len(sub_permute)):
                sub_permute[i].insert(0, n)
                result.append(sub_permute[i])

        return result


s = Solution()
print(s.permute([1, 2, 3]))
print(s.permute([1, 2, 3, 4]))
