class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_du=set(nums)
        return len(nums)!=len(non_du)

        