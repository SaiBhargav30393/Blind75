class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX  = 2**31-1
        def to_u32(x):  # force 32-bit unsigned
            return x & MASK

        def to_i32(x):  # interpret as signed 32-bit
            x &= MASK
            return x if x <= MAX else x - (MASK + 1)
        while b:
            carry = to_u32(a & b)
            a     = to_u32(a ^ b)
            b     = to_u32(carry << 1)
        return to_i32(a)
        