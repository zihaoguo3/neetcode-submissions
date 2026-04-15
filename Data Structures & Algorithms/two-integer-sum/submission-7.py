class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n=len(nums)
        reminder=set()

        for i,x in enumerate(nums):
            need=target-x
            if need in reminder:
                return [nums.index(need),i]
            reminder.add(x)
        

        