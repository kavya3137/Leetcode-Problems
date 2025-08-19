class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        count = 0
        for num in nums:
            if num == 0:
                count += 1
                total += count   
            else:
                count = 0        
        return total

        