class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""

        for c in path + '/':
            if c == '/':
                if curr == '..':
                    if len(stack) != 0:
                        stack.pop()
                elif curr != '' and curr != '.':
                    stack.append(curr)
                
                curr = ""
            else:
                curr += c
            
        return "/" + "/".join(stack)