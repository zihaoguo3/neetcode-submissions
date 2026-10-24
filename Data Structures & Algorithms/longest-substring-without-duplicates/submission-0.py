class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counting={}
        l=0
        res=0
        for r,c in enumerate(s):
            if c in counting and counting[c]>=l:
                l=counting[c]+1
            counting[c]=r
            res=max(res,r-l+1)
        return res

        