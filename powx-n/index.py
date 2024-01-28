class Solution:
    def myPow(self, x: float, n: int) -> float:
        def my(x:float, n: int ) -> float:
            if n == 0:
                return 1
            elif n<0:
                return my(x,n+1)/x
            else:
                return x * my(x,n-1)
        return my(x,n)
solution = Solution()



print(solution.myPow(2,10))