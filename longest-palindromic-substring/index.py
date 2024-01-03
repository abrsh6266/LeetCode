class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        n = len(s)
        while l >=  0:
            i = 0
            while i+l <= n:
                if s[i:i+l] == (s[i:i+l])[::-1]:
                    return s[i:i+l]
                i += 1
            l -= 1
solution = Solution()
print(solution.longestPalindrome('fuckaaacabaaaaccbbbbbcbbbbbb'))