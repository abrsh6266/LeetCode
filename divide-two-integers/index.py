class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if divisor == 0:
            return INT_MAX if dividend > 0 else INT_MIN
        if dividend == 0:
            return 0
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
        result = sign * quotient
        return min(max(result, INT_MIN), INT_MAX)