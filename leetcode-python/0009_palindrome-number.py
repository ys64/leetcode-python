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


class Solution2:
    # 01/23/2021
    def isPalindrome(self, x: int) -> bool:
        # convert int to string
        str_x = str(x)
        is_palindrome = True
        for i, c in enumerate(str_x):

            if len(str_x) / 2 < i:
                break

            if c == str_x[len(str_x) - i - 1]:
                pass
            else:
                is_palindrome = False
                break

        return is_palindrome


class Solution3:
    # 04/12/2021
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        str_x = str(x)

        while len(str_x) != 0 and len(str_x) != 1:
            if str_x[0] != str_x[len(str_x) - 1 :]:
                return False

            str_x = str_x[1 : len(str_x) - 1]

        return True


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
print(s.isPalindrome(-101))

s2 = Solution2()
print(s2.isPalindrome(121))
print(s2.isPalindrome(-121))
print(s2.isPalindrome(10))
print(s2.isPalindrome(-101))

s3 = Solution3()
print(s3.isPalindrome(121))
print(s3.isPalindrome(-121))
print(s3.isPalindrome(10))
print(s3.isPalindrome(-101))
