#Simple solution using defaultdict
from collections import  defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dct=defaultdict(list)
        for s in strs:
            sorted_s="".join(sorted(s))
            dct[tuple(sorted_s)].append(s)
        return dct.values()

#solution using Counter
from collections import Counter, defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dct=defaultdict(list)
        for s in strs:
            c=[0]*26
            for ch in s:
                c[ord(ch)-ord("a")]+=1
            dct[tuple(c)].append(s)
        return dct.values()