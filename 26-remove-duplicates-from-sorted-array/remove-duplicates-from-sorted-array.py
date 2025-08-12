class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st=0
        for last in range(1,len(nums)):
            if nums[last]!=nums[st]:
                st+=1
                
                nums[st]=nums[last]
        return st+1
        