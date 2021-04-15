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


class Solution2:
    # 04/14/2021
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i, l in enumerate(haystack):
            if len(haystack) - i < len(needle):
                break

            if l == needle[0]:
                n_index = 1
                while n_index < len(needle):
                    if haystack[i + n_index] != needle[n_index]:
                        n_index = -1
                        break
                    n_index += 1

                if n_index == len(needle):
                    return i

        return -1


s = Solution()
print(s.strStr("hello", "ll"))
print(s.strStr("hello", "llo"))
print(s.strStr("aaaaa", "bba"))
print(s.strStr("", ""))
print(s.strStr("mississippi", "issipi"))
print(s.strStr("aaa", "aaaaa"))
