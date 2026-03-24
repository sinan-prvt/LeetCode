class Solution:
    def returnToBoundaryCount(self, num: List[int]) -> int:
        position = 0
        count = 0

        for move in num:
            position += move

            if position == 0:
                count += 1
            
        return count