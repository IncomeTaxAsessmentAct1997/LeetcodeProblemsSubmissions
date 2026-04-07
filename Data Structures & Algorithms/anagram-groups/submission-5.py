class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:      
        if not strs: return []
        
        strs_count = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            strs_count[key].append(word)

        return list(strs_count.values())