class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        strs.append('lxs')
        n = len(strs)
        z = []
        r = []
        for i in range(n):
            arr = []
            if i in z:
                continue
            for j in range(i+1,n):
                if j in z:
                    continue
                if j in z and j==i+1:
                    break
                if i not in z:
                    z.append(i)
                    arr.append(strs[i])
                if ''.join(sorted(strs[i])) == ''.join(sorted(strs[j])):
                    arr.append(strs[j])
                    z.append(j)
            r.append(arr)
        r.remove([])
        return r
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) 