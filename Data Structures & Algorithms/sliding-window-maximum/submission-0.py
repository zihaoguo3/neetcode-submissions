from collections import Counter
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        res=[]
        count=Counter()
        for r, x in enumerate(nums):
            count[x]+=1
            if (r-l+1)>k:
                count[nums[l]]-=1
                if count[nums[l]]==0:
                    del count[nums[l]]
                l+=1
            if (r-l+1)==k:
                max_num=float('-inf')
                for key in count:
                    max_num=max(key, max_num)
                res.append(max_num)
        return res




