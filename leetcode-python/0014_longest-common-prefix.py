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


class Solution2:
    # 04/12/2021
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = ""
        base = strs[0]

        for i, c in enumerate(base):
            for s in strs[1:]:
                if len(s) <= i:
                    return base[:i]
                elif s[i] != c:
                    return base[:i]
            prefix += c

        return prefix


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
print(s.longestCommonPrefix([]))
print(s.longestCommonPrefix(["dog"]))
print(s.longestCommonPrefix(["", "dog"]))
print(s.longestCommonPrefix(["ab", "a"]))


s2 = Solution2()
print(s2.longestCommonPrefix(["flower", "flow", "flight"]))
print(s2.longestCommonPrefix(["dog", "racecar", "car"]))
print(s2.longestCommonPrefix([]))
print(s2.longestCommonPrefix(["dog"]))
print(s2.longestCommonPrefix(["", "dog"]))
print(s2.longestCommonPrefix(["ab", "a"]))
