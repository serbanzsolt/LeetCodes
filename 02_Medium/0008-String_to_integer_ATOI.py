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
        result = []
        s = list(s)
        
        # not contain numbers
        if not any(element in s for element in digits):
            return 0
        # empty
        elif len(s) == 0:
            return 0
        
        
        # CHECKING ALL THE ELEMENTS IN "S"
        for i in range(0,len(s)):
            # s[i] is a number
            if s[i] in digits:
                result.append(s[i])
                # checking the next one till the end
                if i < len(s)-1:
                    if s[i+1] in digits:
                        continue
                    else:
                        break
            # s[i] is a "+"
            elif s[i] == "+":
                # "+" is first or only " " before it
                if i == 0 or all([element == " " for element in s[0:i]]):
                    continue
                else:
                    return 0
                
            # s[i] is a "-"
            elif s[i] == "-":
                # "-" is first or only " " before it
                if i == 0 or all([element == " " for element in s[0:i]]):
                    result.append("-")
                else:
                    return 0
                
            # s[i] is a " "
            elif s[i] == " ":
                # " " is first or only " " before it
                if i == 0 or all([element == " " for element in s[0:i]]):
                    continue
                else:
                    return 0
            
            # everything else
            else:
                return 0
                
        result = "".join(result)
        result = int(result)
        if result > ((2 ** 31) -1):
            return ((2 ** 31) -1)
        elif result < (-2 ** 31 ):
            return (-2 ** 31 )
        else:
            return result

my_solution = Solution()

# TEST CASES:

result1 = my_solution.myAtoi("   -42")
result2 = my_solution.myAtoi("42")
result3 = my_solution.myAtoi("-42")
result4 = my_solution.myAtoi("            42")
result5 = my_solution.myAtoi("alma42")
result6 = my_solution.myAtoi("-42almma")
result7 = my_solution.myAtoi("words and 987")
result8 = my_solution.myAtoi("-+4")
result9 = my_solution.myAtoi("00000-42a1234")
result10 = my_solution.myAtoi("-1123u3761867")
result11 = my_solution.myAtoi("-91283472332")
result12 = my_solution.myAtoi("-115579378e25")
result13 = my_solution.myAtoi(".1")
result14 = my_solution.myAtoi("  ")
result15 = my_solution.myAtoi("   +0 123")
result16 = my_solution.myAtoi("  -0012a42")
result17 = my_solution.myAtoi(" a")
result18 = my_solution.myAtoi("abc")
result19 = my_solution.myAtoi("    -88827   5655  U")
result20 = my_solution.myAtoi("  +  413")
result21 = my_solution.myAtoi("  +b12102370352")

print(f'number is: {result1} type: {type(result1)}')
print(f'number is: {result2} type: {type(result2)}')
print(f'number is: {result3} type: {type(result3)}')
print(f'number is: {result4} type: {type(result4)}')
print(f'number is: {result5} type: {type(result5)}')
print(f'number is: {result6} type: {type(result6)}')
print(f'number is: {result7} type: {type(result7)}')
print(f'number is: {result8} type: {type(result8)}')
print(f'number is: {result9} type: {type(result9)}')
print(f'number is: {result10} type: {type(result10)}')
print(f'number is: {result11} type: {type(result11)}')
print(f'number is: {result12} type: {type(result12)}')
print(f'number is: {result13} type: {type(result13)}')
print(f'number is: {result14} type: {type(result14)}')
print(f'number is: {result15} type: {type(result15)}')
print(f'number is: {result16} type: {type(result16)}')
print(f'number is: {result17} type: {type(result17)}')
print(f'number is: {result18} type: {type(result18)}')
print(f'number is: {result19} type: {type(result19)}')
print(f'number is: {result20} type: {type(result20)}')
print(f'number is: {result21} type: {type(result21)}')




# "." as a wierd edge case...
        # elif s[0] == ".":
        #     return 0

# if all([element == " " for element in s[0:i]]):
                #     continue
                # else:
                #     return 0

# # If empty
#         if len(s) == 0:
#             return 0
#         # Starting is " " or "-" or "+"
#         elif s[0] in starting_char:
#             if len(s) > 1:
#                 if s[1] in digits or s[1] == " ":
#                     # s = s.replace(" ", "")
#                     s = list(s)
#                     # print(s)
#                     if s[0] == "-":
#                         result.append("-")
#                         for i in range(1, len(s)):
#                             if s[i] in digits:
#                                 result.append(s[i])
#                             else:
#                                 break
#                     elif s[0] == "+":
#                         for i in range(1, len(s)):
#                             if s[i] in digits:
#                                 result.append(s[i])
#                             else:
#                                 break
#                     elif s[0] == " ":
#                         for i in range(1, len(s)):
#                             # and i < len(s)-1
#                             if s[i] == " " and i == len(s)-1:
#                                 return 0
#                             elif s[i] == " " and not (any(element in s[0:i] for element in digits and starting_char)):
#                                 continue
#                             elif s[i] == " " and (any(element in s[0:i] for element in digits and starting_char)):
#                                 if (any(element in s[0:i] for element in digits) and not any(element in s[0:i] for element in starting_char)):
#                                     print("1")
#                                     break
#                                 elif (any(element in s[0:i] for element in starting_char) and not any(element in s[0:i] for element in digits)):
#                                     print("2")
#                                     return 0
#                             elif s[i] in digits:
#                                 result.append(s[i])
#                             elif s[i] == "+":
#                                 continue
#                             elif s[i] == "-":
#                                 result.append("-")
#                             elif s[i] not in digits and s[i] not in starting_char and (any(element in s[0:i] for element in digits)):
#                                 break
#                             else:
#                                 return 0
#                     else:
#                         for i in range(0, len(s)):
#                             if s[i] in digits:
#                                 result.append(s[i])
#                             else:
#                                 break
#                 else:
#                     return 0
#             else:
#                 return 0
            
#         # Starting is digit 0-9
#         elif s[0] in digits:
#             for i in range(0, len(s)):
#                 if s[i] in digits:
#                     result.append(s[i])
#                 else:
#                     break
#         # Starting is Letter(String)
#         elif s[0] == ".":
#             return 0
#         else:
#             for i in range(0, len(s)):
#                 # next is letter
#                 if s[i] == " ":
#                     return 0
#                 elif s[i] not in digits:
#                     return 0
#                 # next is digit
#                 else:
#                     result.append(s[i])
#                     # not the last
#                     if i < len(s)-1:
#                         # next will be digit
#                         if s[i+1] in digits:
#                             continue
#                         # next will be letter
#                         elif s[i+1] not in digits:
#                             break
#                     # the last one
#                     else:
#                         pass
                    