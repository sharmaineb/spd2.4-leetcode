"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""

class Solution:
    def generate(self, numRows):
        # initialize Pascal's triangle
        triangle = []

        # iterate through each row
        for i in range(numRows):
            # initialize the current row with 1
            row = [1]

            # iterate from the second element to the second last element of the row
            for j in range(1, i):
                # Calculate the value of the current element based on the values of the previous row
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

            # add 1 at the end of the row
            if i > 0:
                row.append(1)

            # add the current row to the triangle
            triangle.append(row)

        return triangle
