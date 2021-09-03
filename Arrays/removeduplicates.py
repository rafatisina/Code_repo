class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums))==0:
            return 0
        else:
            i=1
            val=nums[0]
            for k in range(len(nums)):
                if nums[k] != val:

                    val=nums[k]
                    nums[i]=val
                    i+=1
            return i      
