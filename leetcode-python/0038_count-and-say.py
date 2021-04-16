class Solution(object):
    # 12/17/2020
    def countAndSay(self, n: int) -> str:
        # 1 <= n <= 30
        if n < 1 or 30 < n:
            return ""

        if n == 1:
            return "1"

        previous = self.countAndSay(n - 1)

        curr = 0
        count = 0
        returnValue = ""
        for c in previous:
            if curr == 0:
                curr = int(c)
                count = 1
            elif curr == int(c):
                count += 1
            else:
                returnValue += str(count) + str(curr)
                curr = int(c)
                count = 1

        returnValue += str(count) + str(curr)

        return returnValue


s = Solution()
print(s.countAndSay(4))
print(s.countAndSay(10))
