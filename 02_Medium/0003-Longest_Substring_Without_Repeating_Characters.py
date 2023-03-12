# ==============================================================================
#* Longest Substring Without Repeating Characters
#* Given a string s, find the length of the longest 
#* substring without repeating characters.
# ==============================================================================

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #return len(set(list(s))) # this is wrong it's the longest subsecquence
        s = list(s)
        if len(s) > 0:
            counter = 1
            highest_one = counter
            cached_word = []
            cached_word.append(s[0])
            print(cached_word)
            for i in range(1, len(s)):
                if s[i-1] != s[i] and s[i] not in cached_word:
                    cached_word += s[i]
                    counter += 1
                    print(f"if: {cached_word}")
                    print(f"if: {counter}")
                    if counter > highest_one:
                        highest_one = counter
                elif s[i-1] != s[i] and s[i] in cached_word:
                    cached_word.append(s[i])
                    index = cached_word.index(s[i])
                    print(f"index: {index}")
                    cached_word = cached_word[index+1:]
                    counter = len(cached_word)
                    print(f"elif: {cached_word}")
                    print(f"elif: {counter}")
                    if counter > highest_one:
                        highest_one = counter
                else:
                    cached_word.clear()
                    cached_word.append(s[i])
                    print(f"else: {cached_word}")
                    print(f"else: {counter}")
                    counter = 1
            return highest_one
        else:
            return 0
    
my_solution = Solution()
print(f'LONGEST: {my_solution.lengthOfLongestSubstring("abcabcbb")}') #3
print(f'LONGEST: {my_solution.lengthOfLongestSubstring("bbbbb")}')    #1
print(f'LONGEST: {my_solution.lengthOfLongestSubstring("pwwkew")}')   #3
print(f'LONGEST: {my_solution.lengthOfLongestSubstring("dvdf")}')     #3
print(f'LONGEST: {my_solution.lengthOfLongestSubstring("ckilbkd")}')  #5
print(f'LONGEST: {my_solution.lengthOfLongestSubstring("bpfbhmipx")}')  #7