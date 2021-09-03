class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = 0
        for k in nums:
            if k==0:
                curr_sum = 0
            else:
                curr_sum+=k

            max_sum = max(max_sum, curr_sum)
        return max_sum

        
