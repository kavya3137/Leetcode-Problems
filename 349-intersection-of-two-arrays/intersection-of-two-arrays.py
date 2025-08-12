class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count=Counter(nums1)
        res=[]

        for i in nums2:
            if count[i]>0:
                if i not in res:
                    res.append(i)
                    count[i]-=1
        return res
        