class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        num,i = 0,0
        while i < len(s):
            if i+1<len(s) and (roman[s[i+1]]/roman[s[i]]==10 or roman[s[i+1]]/roman[s[i]]==5):
                num += roman[s[i+1]]-roman[s[i]]
                i += 2
            else:
                num += roman[s[i]]
                i += 1
        return num
solution = Solution()
print(solution.romanToInt("MCMXCIV"))