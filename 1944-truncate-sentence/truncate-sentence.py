class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s1=s.split()
        s2=s1[:k]
        s3=" "
        for i in s2:
            s3+=i+" "
        return s3.strip()
        