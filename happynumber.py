"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
"""

class Solution:
    def isHappy(self, n):
        # set to keep track of seen numbers
        seen = set()

        # continue the process until n becomes 1 (happy) or enters a cycle (unhappy)
        while n != 1:
            # if n is already seen, it enters a cycle, so return False
            if n in seen:
                return False
            seen.add(n)  # add n to the set of seen numbers
            
            # calculate the sum of the squares of digits of n
            n = sum(int(digit) ** 2 for digit in str(n))
        
        # if n becomes 1, it's a happy number, so return True
        return True
