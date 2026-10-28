import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l ,r =1, max(piles)
        res=float('inf')
        while l<=r:
            mid=(l+r)//2
            total_time=0
            for each in piles:
                time=math.ceil(each/mid)
                total_time+=time
            
            if total_time>h:
                l=mid+1
            elif total_time<=h:
                r=mid-1
                res=min(res,mid)
        return res

            