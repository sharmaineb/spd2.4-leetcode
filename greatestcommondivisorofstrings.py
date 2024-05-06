"""
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # define a function to compute the greatest common divisor (GCD) of two numbers
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # get the lengths of both input strings
        len1, len2 = len(str1), len(str2)
        
        # compute the GCD of the lengths of the input strings
        gcd_length = gcd(len1, len2)
        
        # find the common divisor string of length gcd_length
        common_divisor = str1[:gcd_length]

        # check if both input strings can be constructed by repeating the common divisor string
        if str1 == common_divisor * (len1 // gcd_length) and str2 == common_divisor * (len2 // gcd_length):
            # if yes, return the common divisor string
            return common_divisor
        else:
            # if no common divisor string found, return an empty string
            return ""

solution = Solution()
str1 = "ABCABC"
str2 = "ABC"
print(solution.gcdOfStrings(str1, str2))

str1 = "ABABAB"
str2 = "ABAB"
print(solution.gcdOfStrings(str1, str2))

str1 = "LEET"
str2 = "CODE"
print(solution.gcdOfStrings(str1, str2))