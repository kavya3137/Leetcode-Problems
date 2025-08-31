class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if ord(i)>ord(target):
                return i
                break
        else:
            return letters[0]
        