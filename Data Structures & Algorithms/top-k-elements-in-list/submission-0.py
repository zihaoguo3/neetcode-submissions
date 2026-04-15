class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter()
        for num in nums:
            count[num]+=1
        
        return [key for key, freq in count.most_common(k)]
        