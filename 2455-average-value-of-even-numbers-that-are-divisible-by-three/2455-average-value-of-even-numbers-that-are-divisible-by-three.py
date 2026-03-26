class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count = 0
        total = 0

        for num in nums:
            if num % 6 == 0:
                total += num
                count += 1
        return total // count if count else 0