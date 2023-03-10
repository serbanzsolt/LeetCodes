class Solution:
    def isPalindrome(self, x: int) -> bool:
        isPalindrome = False
        number = str(x)
        if number == number[::-1]:
            isPalindrome = True
        return isPalindrome
    
my_solution = Solution()

my_palin = my_solution.isPalindrome(121)
print(my_palin)

my_palin = my_solution.isPalindrome(-121)
print(my_palin)

my_palin = my_solution.isPalindrome(334121433)
print(my_palin)