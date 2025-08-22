class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = set("aeiouAEIOU")
        vowel = consonant = False
        
        for ch in word:
            if not (ch.isdigit() or ch.isalpha()):
                return False
            if ch.isalpha():
                if ch in vowels:
                    vowel = True
                else:
                    consonant = True
        
        return vowel and consonant
