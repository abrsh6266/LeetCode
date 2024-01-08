class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        var = [[''] * len(s) for _ in range(numRows)]
        count = numRows - 2
        index = 0
        column = 0
        while index < len(s):
            for j in range(numRows):
                if index < len(s):
                    var[j][column] = s[index]
                    index += 1
            for j in range(count, 0, -1):
                if index < len(s):
                    var[j][column + 1] = s[index]
                    index += 1
            column += 2
        result = ''.join([''.join(row) for row in var])
        return result

# Example usage:
solution = Solution()
result = solution.convert('PAYPALISHIRING', 3)
print(result)
