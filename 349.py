def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1=set(nums1)
        s2=set(nums2)
        if len(s2)>len(s1):
            s2,s1=s1,s2
        l=[]
        for i in s1:
            if i in s2:
                l.append(i)
        return l