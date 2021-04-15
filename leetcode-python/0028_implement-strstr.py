class Solution:
    # 07/15/2020
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        if len(haystack) < len(needle):
            return -1

        for i, _ in enumerate(haystack):
            if len(haystack) < i + len(needle):
                break

            for j, n in enumerate(needle):
                if haystack[i + j] == n:
                    if j == len(needle) - 1:
                        return i
                else:
                    break

        return -1


s = Solution()
print(s.strStr("hello", "ll"))
print(s.strStr("hello", "llo"))
print(s.strStr("aaaaa", "bba"))
print(s.strStr("", ""))
print(s.strStr("mississippi", "issipi"))
print(s.strStr("aaa", "aaaaa"))
