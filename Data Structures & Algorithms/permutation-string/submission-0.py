from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counting1=Counter()
        counting2=Counter()
        for s in s1:
            counting1[s]+=1
        
        k=len(s1)
        l=0
        for r, s in enumerate(s2):
            counting2[s]+=1
            while (r-l+1)>k:
                counting2[s2[l]]-=1
                if counting2[s2[l]]==0:
                    del counting2[s2[l]]
                l+=1
            if counting1==counting2:
                return True
        return False
                

        