class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst =set()
        l=mx =0 
        for i in range(len(s)):
            while s[i] in lst:
                lst.remove(s[l])
                l+=1
            lst.add(s[i])
            mx=max(mx, i-l+1)
        return mx