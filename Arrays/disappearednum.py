class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #method 1
        for k in range(len(nums)):
            index=abs(nums[k])-1

            if nums[index] > 0:
                nums[index]*=-1
        results=[]


        for k in range(len(nums)):
            if nums[k]>0:
                results.append(k+1)

        return results

#         #method 2
#         hash_table = {}

#         for k in nums:
#             hash_table[k]=1
#         result=[]
#         for num in range(1, len(nums)+1):
#             if num not in hash_table:
#                 result.append(num)
#         return result




            
