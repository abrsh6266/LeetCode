class Solution:
    def reverse(self, x: int) -> int:
        xx = str(x)[::-1]
        val = 0
        if str(x)[0] == '-':
            xx = xx[:-1]
        xxx = ''
        for i in range(len(xx)):
            if xxx == '' and xx[i] == '0':
                continue
            else:
                xxx += xx[i]

        if xxx == '':
            val = 0
        elif str(x)[0] == '-':
            val = int('-' + xxx)
        else:
            val = int(xxx)

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if val < -2**31 or val > 2**31 - 1:
            return 0
        return val
solution = Solution()
print(solution.reverse(120))