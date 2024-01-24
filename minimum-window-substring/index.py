class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(t), len(s)
        if n == 0:
            return ''
        ct, w = {},{}
        for i in range(n):
            ct[t[i]] = 1 + ct.get(t[i],0)
        res,rl = [-1,-1],float('inf')
        n,h = n,0
        l = 0
        for r in range(m):
            x = s[r]
            w[x] = 1 + w.get(x,0)
            if x in ct and w[x] == ct[x]:
                h += 1
            while h == n:
                if (r-l+1) < rl:
                    res = [l,r]
                    rl = r-l+1
                w[s[l]] -= 1
                if s[l] in ct and w[s[l]] < ct[s[l]]:
                    h -= 1
                l += 1
        l,r = res
        return s[l:r+1] if rl != float('inf') else ""
solution = Solution()
print(solution.minWindow("ADOBECODEBANC","ABC")) 