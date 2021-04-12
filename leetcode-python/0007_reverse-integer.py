class Solution:
    # 06/24/2020
    def reverse(self, x: int) -> int:
        # get plus or minus of x
        # save it
        sign = -1 if x < 0 else 1

        # replace x with abs(x)
        x = abs(x)

        ans = 0

        while True:
            # ans * 10
            ans *= 10

            # get the lowest number of x
            lowest = x % 10
            # ans + lowest of x
            ans += lowest

            # replace x with the rest of x
            x //= 10

            # if x is 0 return
            if x == 0:
                break

        ans *= sign

        # if ans is not in the range of 32-bit integer, return 0
        if ans < -2147483648 or 2147483647 < ans:
            return 0

        return ans


s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(0))
