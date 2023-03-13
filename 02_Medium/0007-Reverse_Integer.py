# ==============================================================================
#* Reverse Integer
#* Given a signed 32-bit integer x, return x with its digits reversed. 
#* If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# ==============================================================================

class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x)[::-1])
        if "-" in x:
            x.pop()
            x.insert(0, "-")
        x = int("".join(x))
        if x >= (-2 ** 31) and x <= (2 ** 31 - 1):
            return x
        else:
            return 0

my_solution = Solution()
result = my_solution.reverse(120)
print(f"{result} and the type: {type(result)}")