class Solution:
    def nthSuperUglyNumber(self, n: int, p: list[int]) -> int:
        u = [1]
        i = [0]*len(p)
        for _ in range(1, n):
            x = min(p[j]*u[i[j]] for j in range(len(p)))
            u.append(x)
            for j in range(len(p)):
                if x == p[j]*u[i[j]]:
                    i[j] += 1
        return u[-1]