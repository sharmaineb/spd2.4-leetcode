"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        # define a set of vowels
        vowels = set("aeiouAEIOU")
        # convert the string into a list of characters for easy swapping
        s = list(s)
        # initialize two pointers, one starting from the beginning and the other from the end
        left, right = 0, len(s) - 1

        # iterate until the two pointers meet
        while left < right:
            # move the left pointer forward until it reaches a vowel
            while left < right and s[left] not in vowels:
                left += 1
            # move the right pointer backward until it reaches a vowel
            while left < right and s[right] not in vowels:
                right -= 1
            # swap the vowels found at positions left and right
            s[left], s[right] = s[right], s[left]
            # move the pointers to the next positions
            left += 1
            right -= 1

        # convert the list of characters back to a string and return
        return ''.join(s)

solution = Solution()
s1 = "hello"
print(solution.reverseVowels(s1))

s2 = "leetcode"
print(solution.reverseVowels(s2))