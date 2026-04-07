class Solution:

    def encode(self, strs: List[str]) -> str:
            for x in range(len(strs)):
                strs[x] = f"{len(strs[x])}#{strs[x]}"

            return "".join(strs)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]

            decoded.append(word)

            i = j + 1 + length

        return decoded
    
print(Solution().decode(Solution().encode(["we","say",":","yes","!@#$%^&*()"])))