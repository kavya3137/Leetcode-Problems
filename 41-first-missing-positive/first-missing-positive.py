class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        for i in range(1,len(nums)+5):
            if i not in nums_set:
                if i>0:
                    return i
                    break
