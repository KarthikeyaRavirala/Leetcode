class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = result = 0
        seen = dict()
        for i, c in enumerate(s):
            if seen.get(c, -1) >= start:
                start = seen[c] + 1
            result = max(result, i - start + 1)
            seen[c] = i
        return result
        
