class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

#         maxlength=0
#         #Brute Force solution
#         for k in range (len(nums)):
#             numzero=0
#             for j in range(k, len(nums)):
#                 if numzero == 2:
#                     break

#                 if nums[j] == 0:
#                     numzero+=1

#                 if numzero==1:
#                     maxlength = max (maxlength, j-k+1)
#         return maxlength


    #two-pointer approach
        left=-1
        right=-1
        maxlengh=0
        numzeros=0
        while right < len(nums)-1:
            right += 1
            if nums[right] == 0:
                numzeros += 1

            while numzeros==2:
                left += 1
                if nums[left]==0:
                    numzeros-=1;

            maxlengh=max(maxlengh,right-left)
        return maxlengh         
