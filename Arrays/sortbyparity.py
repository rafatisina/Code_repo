class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # return([x for x in nums if x%2 == 0]+[x for x in nums if x%2 == 1])

        i=0
        j=len(nums)-1

        while i < j:
            if A[i] % 2 > A[j] %2:
                A[i], A[j] = A[j], A[i]

            if A[i]%2 == 0: i+=1
            if A[j]%2 == 1: j-=1

        
