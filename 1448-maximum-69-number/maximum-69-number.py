class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        for i in s:
            if i=="6":
                s = s.replace('6', '9', 1)
                break
        return int(s)
        