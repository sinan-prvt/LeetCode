class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digit_sum = 0
        num = x

        while num > 0:
            digit_sum += num % 10
            num //= 10

        if x % digit_sum == 0:
            return digit_sum
        else:
            return -1