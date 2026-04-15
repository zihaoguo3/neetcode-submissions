class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count=defaultdict(list)

        for each in strs:
            key=''.join(sorted(each))
            count[key].append(each)
        return list(count.values())