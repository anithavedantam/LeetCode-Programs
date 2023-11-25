class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return
        if len(s) == 1:
            return s
        stack = []
        for c in s:
            if stack and c.swapcase() == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)