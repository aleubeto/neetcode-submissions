class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            prefix = f"{len(word)}#"
            output += f"{prefix}{word}"
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        start = 0
        while start < len(s):
            end = start
            while s[end] != "#":
                end += 1
            length = int(s[start:end])
            word = s[(end+1):(end+1+length)]
            output.append(word)
            start = end+1+length
        return output
