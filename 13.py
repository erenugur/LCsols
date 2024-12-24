class Solution:
    def romanToInt(self, s: str) -> int:
        val = 0
        i = 0
        while i < len(s):
            if i < (len(s)-1) and s[i] == 'I' and s[i+1] == 'V':
                val += 4
                i += 2
            elif i < (len(s)-1) and s[i] == 'I' and s[i+1] == 'X':
                val += 9
                i += 2
            elif i < (len(s)-1) and s[i] == 'X' and s[i+1] == 'L':
                val += 40
                i += 2
            elif i < (len(s)-1) and s[i] == 'X' and s[i+1] == 'C':
                val += 90
                i += 2
            elif i < (len(s)-1) and s[i] == 'C' and s[i+1] == 'D':
                val += 400
                i += 2
            elif i < (len(s)-1) and s[i] == 'C' and s[i+1] == 'M':
                val += 900
                i += 2
            elif s[i] == 'I':
                val += 1
                i += 1
            elif s[i] == 'V':
                val += 5
                i += 1
            elif s[i] == 'X':
                val += 10
                i += 1
            elif s[i] == 'L':
                val += 50
                i += 1
            elif s[i] == 'C':
                val += 100
                i += 1
            elif s[i] == 'D':
                val += 500
                i += 1
            elif s[i] == 'M':
                val += 1000
                i += 1
        return val
            
