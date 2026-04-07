class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)

        for string in strs:
            hash_map = defaultdict(int)
            for char in string:
                hash_map[char] += 1

            key = tuple(sorted(hash_map.items()))
            final[key].append(string)

        return list(final.values())