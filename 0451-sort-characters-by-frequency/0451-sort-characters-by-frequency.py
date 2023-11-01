class Solution:
    def frequencySort(self, s: str) -> str:
        seen = {}
        for c in s:
            if c not in seen:
                seen[c] = 1
            else:
                seen[c] += 1
        st = ""
        for i in sorted(seen.items() , key = lambda x:x[1]):
            st += i[0] * i[1]
        
        return st[::-1]
        
        
        