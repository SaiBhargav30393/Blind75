#Easy Solution
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s)==Counter(t)
        
#Solution 2
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        countS=[0]*26
        countT=[0]*26
        for i in range(len(s)):
            countS[ord(s[i])-ord('a')]+=1
            countT[ord(t[i])-ord('a')]+=1
        return countS==countT