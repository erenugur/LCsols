class Solution:
    def isValid(self, s: str) -> bool:
        charList = []
        trackCharList = 0
        for i in range(len(s)):
            if (s[i] == '(') or (s[i] == '{') or (s[i] == '['):
                if (s[i] == '('):
                    charList.append('(')
                elif (s[i] == '{'):
                    charList.append('{')
                elif (s[i] == '['):
                    charList.append('[')
            elif (s[i] == ')') or (s[i] == '}') or (s[i] == ']'):
                if (i == 0) or (trackCharList == 0):
                    return False
                elif (s[i] == ')'):
                    if (charList[trackCharList-1] == '('):
                        charList.pop()
                        trackCharList -= 2
                    else:
                        return False
                elif (s[i] == '}'):
                    if (charList[trackCharList-1] == '{'):
                        charList.pop()
                        trackCharList -= 2
                    else:
                        return False
                elif (s[i] == ']'):
                    if (charList[trackCharList-1] == '['):
                        charList.pop()
                        trackCharList -= 2
                    else:
                        return False
            trackCharList += 1
        if not charList:
            return True
        return False
