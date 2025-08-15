class Solution(object):
    def maxSubArray(self, nums):
        ##kadanes
        l_max, g_max= float('-inf'),float('-inf')
        for num in nums:
            l_max=max(num, l_max+num)
            g_max=max(l_max, g_max)
        return g_max