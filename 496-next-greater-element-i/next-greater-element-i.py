class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
            index=nums2.index(i)
            found=-1
            for j in range(index+1,len(nums2)):
                if nums2[j]>i:
                    found=nums2[j]
                    break
            res.append(found)  
        return res  
        