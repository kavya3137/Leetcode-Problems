import math

class Solution:
    def canMeasureWater(self, x: int, y: int, t: int) -> bool:
        if t > x + y:
            return False
        return t % math.gcd(x, y) == 0
