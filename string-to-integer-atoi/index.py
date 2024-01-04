class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        signed = ''
        number = ''
        i = 0
        while i < n and s[i] == ' ':
            i += 1
        if i < n and (s[i] == '-' or s[i] == '+'):
            signed = s[i]
            i += 1
        while i < n and s[i].isdigit():
            number += s[i]
            i += 1
        if len(number) == 0:
            return 0
        val = int(signed + number)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        return max(min(val, INT_MAX), INT_MIN)