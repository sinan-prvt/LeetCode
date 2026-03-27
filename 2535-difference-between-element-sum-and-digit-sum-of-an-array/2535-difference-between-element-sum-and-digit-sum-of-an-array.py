class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0

        for num in nums:
            while num > 0:
                digit_sum += num % 10
                num //= 10
            
        return element_sum - digit_sum