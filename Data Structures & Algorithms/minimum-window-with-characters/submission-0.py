from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict1=Counter()
        dict2=Counter(t)
        l=0
        have, required = 0, len(dict2)
        best_len = float('inf')
        best_l = 0
        for r, x in enumerate(s):
            dict1[x]+=1
            if x in dict2 and dict1[x]==dict2[x]:
                have+=1
            while have==required:
                if (r-l+1)<best_len:
                    best_len=r-l+1
                    best_l=l
                dict1[s[l]]-=1
                if s[l] in dict2 and dict1[s[l]]<dict2[s[l]]:
                    have-=1
                l+=1
        return "" if best_len==float('inf') else s[best_l:best_l+best_len]
            
                


        