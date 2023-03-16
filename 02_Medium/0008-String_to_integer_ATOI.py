# ==============================================================================
#* String to integer (Atoi)
"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
"""
# ==============================================================================

class Solution:
    def myAtoi(self, s: str) -> int:
        digits = ["0","1","2","3","4","5","6","7","8","9"]
        starting_char = [" ","+","-"]
        result = []
        # Starting is " " or "-" or "+"
        if s[0] in starting_char:
            s = s.replace(" ", "")
            s = list(s)
            print(s)
            if s[0] == "-":
                result.append("-")
                for i in range(1, len(s)):
                    if s[i] in digits:
                        result.append(s[i])
                    else:
                        break
            else:
                for i in range(0, len(s)):
                    if s[i] in digits:
                        result.append(s[i])
                    else:
                        break
        # Starting is digit 0-9
        elif s[0] in digits:
            for i in range(0, len(s)):
                if s[i] in digits:
                    result.append(s[i])
                else:
                    break
        # Starting is Letter(String)
        else:
            for i in range(0, len(s)):
                # next is letter
                if s[i] not in digits:
                    pass
                # next is digit
                else:
                    result.append(s[i])
                    # not the last
                    if i < len(s)-1:
                        # next will be digit
                        if s[i+1] in digits:
                            continue
                        # next will be letter
                        elif s[i+1] not in digits:
                            break
                    # the last one
                    else:
                        pass
        result = "".join(result)
        result = int(result)
        return result

my_solution = Solution()
print(f'number is:{my_solution.myAtoi("42")} type: {my_solution.myAtoi("42")}')
print(f'number is:{my_solution.myAtoi("-42")} type: {my_solution.myAtoi("-42")}')
print(f'number is:{my_solution.myAtoi("            42")} type: {my_solution.myAtoi("            42")}')
print(f'number is:{my_solution.myAtoi("alma42")} type: {my_solution.myAtoi("alma42")}')
print(f'number is:{my_solution.myAtoi("-42almma")} type: {my_solution.myAtoi("-42almma")}')