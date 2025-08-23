class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        unique = nums.index(largest)
        
        for n in nums:
            if n != largest and largest < 2 * n:
                return -1
        return unique
