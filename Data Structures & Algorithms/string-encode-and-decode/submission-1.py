class Solution:

    def encode(self, strs: List[str]) -> str:

        newStr = ""
        for i in range(len(strs)):
            newStr = newStr + str(len(strs[i])) + "#" + strs[i]
        return newStr

        # newStr = []
        # for word in strs:
        #     newStr.append(f"{len(word)}#{word}")
        # return "".join(newStr)

    def decode(self, s: str) -> List[str]:

        count = 0
        newStr = []
        i = 0
        while i < len(s):
            while s[i] != "#":
                count = int(s[i]) + 10 * count
                i += 1
            i += 1
            word = s[i:count+i]
            newStr = newStr + [word]
            i += count
            count = 0
        return list(newStr)
            