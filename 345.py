class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_string = "aeiouAEIOU"
        vowel_list = []
        return_s = ""
        for i in range(len(s)):
            if s[i] in vowel_string:
                vowel_list.append(s[i])

        print(vowel_list)

        for i in range(len(s)):
            if s[i] in vowel_string:
                if (len(vowel_list) > 1):
                    return_s += vowel_list[len(vowel_list) - 1]
                    vowel_list.pop()
                else:
                    return_s += vowel_list[0] 
            else:
                return_s += s[i]
        return return_s
            
