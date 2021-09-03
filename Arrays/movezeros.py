class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if (len(nums))==0:
            return 0
        wr = 0
        for rr in range(len(nums)):
            if nums[rr]!= 0:
                nums[wr] = nums [rr]
                wr+=1
        nums[wr:]=[0]*(len(nums)-wr)

        return nums
