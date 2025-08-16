#solution 1(Not optimal) nlogn
class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for n in range(n+1):
            c=0
            while n!=0:
                n= n&n-1
                c+=1
            res.append(c)
        return res

#solution 2- using dp - n
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        offset=1
        for i in range(1, n+1):
            if offset*2==i:
                offset=i
            ans[i]=1+ans[i-offset]
        return ans    
