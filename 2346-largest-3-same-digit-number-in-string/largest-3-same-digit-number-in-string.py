class Solution:
    def largestGoodInteger(self, num: str) -> str:
        s1 = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                s1 = max(s1, num[i:i+3])
        return s1

        