class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set=set()
        l=0
        maxl=0
        for r in range(len(s)):
            while s[r] in Set:
                Set.remove(s[l])
                l+=1
            Set.add(s[r])
            maxl=max(maxl,r-l+1)
        return maxl
