class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_max= l_min= g_max = nums[0]
        for i in range(1,len(nums)):
            prev_min=l_min
            l_min= min(nums[i], nums[i]* l_max, nums[i]*l_min)
            l_max= max(nums[i], nums[i]* l_max, nums[i]*prev_min)
            g_max= max(l_max, g_max)
        return g_max
        