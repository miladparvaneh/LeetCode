class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                output += word1[i]
            if i < len(word2):
                output += word2[i]

        return output
