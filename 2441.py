class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        start=0
        end=len(nums)-1
        while(start<end):
            if nums[start]>=0:
                break
            if -1*(nums[start])==nums[end]:
                return nums[end]
            elif -1*(nums[start])>nums[end]:
                start +=1
            else:
                end-=1
        return -1