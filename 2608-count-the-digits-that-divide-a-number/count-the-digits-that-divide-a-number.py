class Solution:
    def countDigits(self, num: int) -> int:
        if num<=9:
            return 1
        else:
            n1=num
            s=str(num)
            s1=0
            for i in s:
                if n1%int(i)==0:
                    s1+=1
            return s1

        