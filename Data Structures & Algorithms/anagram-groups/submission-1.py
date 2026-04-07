class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)
        for string in strs:
            current_string = [0] * 26
            for char in string:
                current_string[ord(char) - 97] += 1
            final[tuple(current_string)].append(string)

        return list(final.values()) 
