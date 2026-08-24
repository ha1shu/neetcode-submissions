class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        count_stack = []
        cur = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k*10 + int(c)

            elif c == '[':
                string_stack.append(cur)
                count_stack.append(k)
                k = 0
                cur = ""
            elif c == ']':
                temp = cur
                cur = string_stack.pop()
                count = count_stack.pop()
                cur += temp * count
            else:
                cur +=c
        return cur