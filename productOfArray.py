lass Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l= len(nums)
        arr=[1]*l
        lf, rf =1,1
        for i in range(l):
            arr[i]=lf
            lf*= nums[i]
        for i in range(l-1,-1,-1):
            arr[i]*= rf
            rf*= nums[i]
        return arr
        