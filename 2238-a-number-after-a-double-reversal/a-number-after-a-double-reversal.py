class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num)
        r = s[::-1]
        n = int(r)
        rr = int(str(n)[::-1])
        return rr == num

        
        