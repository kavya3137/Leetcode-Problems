class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l1 = []
        for i in range(len(nums)):
            if nums[i] != val:
                l1.append(nums[i])
        for i in range(len(l1)):
            nums[i] = l1[i]
        for i in range(len(l1), len(nums)):
            nums[i] = "_"
        return len(l1)

        