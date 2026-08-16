class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_list = list(word1)
        word2_list = list(word2)
        i = 0
        j = 0
        result = []
        while i < len(word1_list) and j< len(word2_list):
            result.append(word1_list[i])
            result.append(word2_list[j])
            i+=1
            j+=1

        while i<len(word1_list):
            result.append(word1_list[i])
            i+=1
        while j<len(word2_list):
            result.append(word2_list[j])
            j+=1
        
        resulString = "".join(result)
        return resulString