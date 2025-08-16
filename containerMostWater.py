class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, h= 0, len(height)-1
        area=float("-inf")
        while l<h:
            area= max(area,(h-l)*min(height[l],height[h]))
            if height[l]<height[h]:
                l+=1
            else:
                h-=1
        return area