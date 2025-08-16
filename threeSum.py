class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        "nlogn+n2"
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l, h = i+1, len(nums)-1
            while l<h:
                sm= nums[i]+nums[l]+nums[h]
                if sm>0:
                    h-=1
                elif sm<0:
                    l+=1
                else:
                    result.append([nums[i], nums[l], nums[h]])
                    l+=1
                    h-=1
                    while l<h and nums[l]==nums[l-1]:
                        l+=1
                    while l<h and nums[h]==nums[h+1]:
                        h-=1
        return result
