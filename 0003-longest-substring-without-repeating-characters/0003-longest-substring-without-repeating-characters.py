class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len



# Another method HashMap insted of Set

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         char_set = {}
#         left = 0
#         max_len = 0

#         for right in range(len(s)):
#             if s[right] in char_set:
#                 left = max(left, char_set[s[right]] + 1)
#             char_set[s[right]] = right
#             max_len = max(max_len, right - left + 1)
#         return max_len