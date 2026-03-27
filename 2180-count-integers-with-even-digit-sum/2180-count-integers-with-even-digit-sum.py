class Solution:
    def countEven(self, n: int) -> int:
        count = 0

        for i in range(1, n + 1):
            digit_sum = 0
            num = i

            while num > 0:
                digit_sum += num % 10
                num //= 10
            
            if digit_sum % 2 == 0:
                count += 1
        
        return count