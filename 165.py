class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1=version1.split('.')
        l2=version2.split('.')
        x=0
        if len(l1)>len(l2):
            for i in range(len(l1)-len(l2)):
                l2.append('0')
        elif len(l1)<len(l2):
            for i in range(len(l2)-len(l1)):
                l1.append('0')
        mul=1
        for i in l1[::-1]:
            x+=mul*int(i)
            mul*=10
        y=0
        mul=1
        for i in l2[::-1]:
            y+=mul*int(i)
            mul*=10
        print(x,y)
        if x<y:
            return -1
        elif x==y:
            return 0
        else:
            return 1
    