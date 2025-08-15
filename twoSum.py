class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dct={}
        for i in range(len(nums)):
            num=target-nums[i]
            if num in dct:
                return [i,dct[num]]
            dct[nums[i]]=i