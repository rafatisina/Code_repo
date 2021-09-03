class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # #brute_force
        # squares = []
        # for k in nums:
        #     squares.append(k*k)
        # squares.sort()
        # return squares

        #two pointer
        n=len(nums)
        left=0
        right=n-1
        result = [0]*len(nums)
        cntr=right
        for k in range(n-1,-1,-1):
            if abs(nums[left]) < abs(nums[right]):
                result[k]=nums[right]*nums[right]
                right-=1
            else:
                result[k]=nums[left]*nums[left]
                left+=1

        return result

    
