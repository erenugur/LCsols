class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        myString = ""
        if len(word1) == len(word2):
            for i in range(len(word1)):
                myString += word1[i]
                myString += word2[i]
        elif len(word1) < len(word2):
            for i in range(len(word1)):
                myString += word1[i]
                myString += word2[i]
            myString += word2[len(word1):len(word2)]
        else:
            for i in range(len(word2)):
                myString += word1[i]
                myString += word2[i]
            myString += word1[len(word2):len(word1)]
        
        return myString
