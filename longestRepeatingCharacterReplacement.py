class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dct={}
        l =re=0
        for r in range(len(s)):
            dct[s[r]]=1+dct.get(s[r],0)
            while (r-l+1)-max(dct.values())>k:
                dct[s[l]]-=1
                l+=1
            re=max(r-l+1, re)
        return re