def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=[]
        for key in d:
            print("d[key]=",d[key],n/3)
            if d[key]>(n/3):
                l.append(key)
        return l