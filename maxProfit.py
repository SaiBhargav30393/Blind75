class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_p=0
        min_v=float('inf')
        for price in prices:
            if min_v>price:
                min_v=price
            else:
                max_p=max(max_p, price-min_v)
        return max_p