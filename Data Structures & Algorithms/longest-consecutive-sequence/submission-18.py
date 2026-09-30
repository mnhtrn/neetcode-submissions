class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seq_len = 0
        max_seq_len = 0

        for i in nums_set:
            if i - 1 not in nums_set:
                seq_len = 0
                while (i + seq_len) in nums_set:
                    seq_len += 1
                max_seq_len = max(max_seq_len, seq_len)
        
        return max_seq_len