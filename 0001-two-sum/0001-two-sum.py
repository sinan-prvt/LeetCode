class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i




# -- Two Pointer

# class Solution:
#     def twoSum(self, arr: List[int], target: int) -> List[int]:
#         arr_with_index = list(enumerate(arr))
#         arr_with_index.sort(key=lambda x: x[1])

#         left = 0
#         right = len(arr) - 1

#         while left < right:
#             current_sum = arr_with_index[left][1] + arr_with_index[right][1]

#             if current_sum == target:
#                 return [arr_with_index[left][0], arr_with_index[right][0]]
#             elif current_sum < target:
#                 left += 1
#             else:
#                 right -= 1
#         return None
