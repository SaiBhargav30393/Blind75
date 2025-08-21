class Solution:

    def encode(self, strs: List[str]) -> str:
        dc=""
        for s in strs:
            dc+=str(len(s))+'#'+s
        return dc
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            ln=int(s[i:j])
            res.append(s[j+1:ln+j+1])
            i=ln+j+1
        return res