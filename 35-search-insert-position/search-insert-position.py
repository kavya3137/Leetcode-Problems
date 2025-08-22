class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, stop = 0, len(nums) - 1
        while start <= stop:
            mid = (start + stop) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                stop = mid - 1
        return start

        