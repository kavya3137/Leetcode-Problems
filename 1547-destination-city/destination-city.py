class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = {a for a, b in paths}
        for a, b in paths:
            if b not in starts:
                return b

        