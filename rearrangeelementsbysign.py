def rearrangeArray(self, nums: List[int]) -> List[int]:
        l1=[]
        l2=[]
        l=[]
        for i in nums:
            if i<0:
                l2.append(i)
            else:
                l1.append(i)
        print(l1,l2)
        for i in range(len(l2)):
            l.extend([l1[i],l2[i]])
        return l
        