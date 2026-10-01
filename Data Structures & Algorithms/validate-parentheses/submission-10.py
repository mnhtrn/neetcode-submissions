class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in {"(", "[", "{"}:
                stack.append(i)
            elif i == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif i == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif i == "]":
                if not stack or stack.pop() != "[":
                    return False
            else:
                return False

        return not stack