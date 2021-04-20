class Solution(object):
    # 07/21/2020
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        for i, c in enumerate(s):
            # print(i, c, s[i:])
            for j, d in enumerate(s[i + 1 :]):
                # print(j, d)
                # print(s[i + 1 : i + 2 + j])
                # print(s[i : i + 1 + j])
                if d in s[i : i + 1 + j]:
                    # print(f"found {d} in {i + 1+ j}")
                    max_length = max(j + 1, max_length)
                    # print("max_length", max_length)
                    break
            else:
                max_length = max(len(s[i:]), max_length)

            # print("--")

        return max_length


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring(""))
print(s.lengthOfLongestSubstring("au"))
print(s.lengthOfLongestSubstring("dvdf"))
