from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        countS= {}
        countT=Counter(t)
        Have, Need = 0, len(countT)
        left,mx=0, float("inf")
        res=""
        for right in range(len(s)):
            countS[s[right]]=1+countS.get(s[right], 0)
            if s[right] in countT and countS[s[right]]==countT[s[right]]:
                Have+=1
            while Have==Need:
                if right-left+1<mx:
                    res=s[left:right+1]
                    mx=len(res)
                if s[left] in countT and countS[s[left]]==countT[s[left]]:
                    Have-=1
                countS[s[left]]-=1
                left+=1
        return res 