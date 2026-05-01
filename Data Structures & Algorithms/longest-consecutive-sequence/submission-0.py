class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        best_len = 0
        best_start = None

        for i in seen:
            if (i-1) not in seen:
                length = 1
                while i+length in seen:
                    length += 1
                best_len = max(best_len, length)
        
        return best_len


        