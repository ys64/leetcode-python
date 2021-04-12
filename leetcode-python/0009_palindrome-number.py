class Solution:
    # 06/30/2020
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        # x must be positive

        # convert integer to string

        str_x = str(x)

        # classification 1 (len(string) is even)
        if len(str_x) % 2 == 0:
            # from 0 - len(string) / 2
            for i in range(len(str_x) // 2):
                print(i, str_x[i], str_x[len(str_x) - 1 - i])
                # if string[0] == string[len(string) - 1] okay
                if str_x[i] == str_x[len(str_x) - 1 - i]:
                    continue
                else:
                    return False

            return True

        # classification 2 (len(string) is odd)
        # same as even length
        else:
            for i in range(len(str_x) // 2):
                if str_x[i] == str_x[len(str_x) - 1 - i]:
                    continue
                else:
                    return False

            return True

        return False


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
print(s.isPalindrome(-101))
