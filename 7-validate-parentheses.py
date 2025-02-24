class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        opening_bracket_arr = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                opening_bracket_arr.append(char)                
            elif len(opening_bracket_arr) != 0 and (
                char == ")" or char == "]" or char == "}"
            ):
                stack_top = opening_bracket_arr.pop()

                if char == ")":
                    if stack_top != "(":
                        return False                    
                elif char == "]":
                    if stack_top != "[":
                        return False                    
                elif char == "}":
                    if stack_top != "{":
                        return False                    
            elif len(opening_bracket_arr) == 0 and (
                char == ")" or char == "]" or char == "}"
            ):
                return False

        if len(opening_bracket_arr) != 0:
            return False
        return True

# URL - https://neetcode.io/problems/validate-parentheses