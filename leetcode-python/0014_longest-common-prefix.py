from typing import List


class Solution:
    # 07/14/2020
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        ans = ""
        # get first element
        base = strs[0]

        for i, c in enumerate(base):
            print(i, c)
            # compare first element's first letter
            for s in strs[1:]:
                print(s)
                if len(s) < i + 1:
                    return ans
                if s[i] == c:
                    pass
                else:
                    return ans
                ans = base[0 : (i + 1)]

        return ans


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
print(s.longestCommonPrefix([]))
print(s.longestCommonPrefix(["dog"]))
print(s.longestCommonPrefix(["", "dog"]))
print(s.longestCommonPrefix(["ab", "a"]))
