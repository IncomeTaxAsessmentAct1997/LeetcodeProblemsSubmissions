class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = defaultdict(int)
        t_hash = defaultdict(int)
        for i in s:
            s_hash[i] += 1
        for i in t:
            t_hash[i] += 1
        
        return s_hash == t_hash