class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        char_array = list(s)
        left = 0
        right = len(s)-1
        while left < right:
            char_array[left],char_array[right] = char_array[right],char_array[left]
            left +=1
            right -=1

        result = "".join(char_array)

        if s == result:
            return True
        else:
            return False
