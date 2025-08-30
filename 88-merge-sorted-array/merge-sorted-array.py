class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l3 = []
        for i in range(m):
            l3.append(nums1[i])
        for j in range(n):
            l3.append(nums2[j])
        l3.sort()
        for i in range(m + n):
            nums1[i] = l3[i]

        