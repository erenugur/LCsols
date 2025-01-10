class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        returnStr = ""
        numOccurences1 = 0
        numOccurences2 = 0

        if len(str1) > len(str2):
            for i in range(len(str2)):
                if str1[i] == str2[i]:
                    returnStr += str1[i]
                else:
                    break
            numOccurences1 = str1.count(returnStr)
            numOccurences2 = str2.count(returnStr)
            while ((numOccurences1 * len(returnStr)) != len(str1)) or ((numOccurences2 * len(returnStr)) != len(str2)):
                returnStr = returnStr[:-1]  # removes the last element of returnStr
                if len(returnStr) == 0:
                    break
                numOccurences1 = str1.count(returnStr)
                numOccurences2 = str2.count(returnStr)
        elif len(str1) < len(str2):
            for i in range(len(str1)):
                if str1[i] == str2[i]:
                    returnStr += str1[i]
                else:
                    break
            numOccurences1 = str1.count(returnStr)
            numOccurences2 = str2.count(returnStr)
            while ((numOccurences2 * len(returnStr)) != len(str2)) or ((numOccurences1 * len(returnStr)) != len(str1)):
                returnStr = returnStr[:-1]  # removes the last element of returnStr
                if len(returnStr) == 0:
                    break
                numOccurences1 = str1.count(returnStr)
                numOccurences2 = str2.count(returnStr)
        elif len(str1) == len(str2):
            for i in range(len(str1)):
                if str1[i] == str2[i]:
                    returnStr += str1[i]
                else:
                    return ""
        
        return returnStr
                
