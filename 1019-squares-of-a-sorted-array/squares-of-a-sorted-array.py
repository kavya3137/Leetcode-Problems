class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l1=[]
        for i in nums:
            l1.append(i**2)
        return sorted(l1)
        