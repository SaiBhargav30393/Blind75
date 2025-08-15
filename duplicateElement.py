class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dct={}
        for num in nums:
            if num in dct:
                return True
            dct[num]=num
        return False
        