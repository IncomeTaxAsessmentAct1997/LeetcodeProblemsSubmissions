class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        
        for x in strs:
            if x == "":
                parts.append("#")
                continue
            
            for i in x:
                parts.append(str(ord(i)))
                parts.append(" ")
            
            parts.append("#")
        
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        decoded = []
        string = ""
        char = ""
        for x in s:
            if x != " " and x != "#":
                char += x
                continue
            elif x == " ":
                string += chr(int(char))
                char = ""
                continue
            elif x == "#":
                decoded.append(string)
                string = ""
                continue
        return decoded