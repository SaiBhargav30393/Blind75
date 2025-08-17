#optimal solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)+1
        sm= (l*(l-1))//2
        for num in nums:
            sm-=num
        return sm

#My solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=set(nums)
        for i in range(len(nums)+1):
            if i not in s:
                return i