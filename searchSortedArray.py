class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, h= 0, len(nums)-1
        while l<=h:
            m= (l+h)//2
            if nums[m]==target:
                return m
            elif nums[l]<=nums[m]:
                if nums[l]<=target<nums[m]:
                    h=m-1
                else:
                    l=m+1
            else:
                if nums[m]<target<=nums[h]:
                    l=m+1
                else:
                    h=m-1
        return -1