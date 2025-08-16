"Solution 1"
class Solution:
    def hammingWeight(self, n: int) -> int:
        r=0 
        while n!=0:
            r += n%2
            n = n>>1
        return r



"Solution 2"
class Solution:
    def hammingWeight(self, n: int) -> int:
        r=0
        while n!=0:
            n=n & n-1
            r+=1
        return r