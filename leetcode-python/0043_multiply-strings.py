class Solution:
    # 6/8/2021
    def multiply(self, num1: str, num2: str) -> str:
        def convertStringNumToInt(num: str) -> int:
            converted = 0
            for c in num:
                i = int(c)
                converted = converted * 10 + i
            return converted

        def convertIntNumToString(num: int) -> str:
            """
            Convert integer to string.
            Or, simply return str(num)?
            """
            if num == 0:
                return "0"

            converted = ""
            while 0 < num:
                c = str(num % 10)
                converted = c + converted
                num = num // 10
            return converted

        i1 = convertStringNumToInt(num1)
        i2 = convertStringNumToInt(num2)

        return convertIntNumToString(i1 * i2)


s = Solution()
print(s.multiply("2", "3"))
print(s.multiply("123", "456"))
print(s.multiply("0", "0"))
print(s.multiply("1", "0"))
print(s.multiply("0", "1"))
