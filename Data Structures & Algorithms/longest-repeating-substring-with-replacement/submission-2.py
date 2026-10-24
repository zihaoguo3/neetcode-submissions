from collections import Counter 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        count=Counter()
        res=0
        for r, c in enumerate(s):
            count[c]+=1
            while (r-l+1)-max(count.values())>k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
            

            
