class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dct = {')':'(', '}':'{', ']':'['}
        res=[]
        for ch in s:
            if ch in dct.values():
                res.append(ch)
            else:
                if len(res)==0 or res.pop()!=dct[ch]:
                    return False
        return True if len(res)==0 else False