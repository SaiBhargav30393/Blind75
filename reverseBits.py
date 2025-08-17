class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0
        for i in range(32):
            res=res<<1
            r=n&1
            res |=r
            n=n>>1

        return res