"""
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""

class Solution:
    def dailyTemperatures(self, temperatures):
        # initialize an empty stack to keep track of indices
        stack = []
        # initialize an array to store the result, initially filled with zeros
        result = [0] * len(temperatures)
        
        # iterate through each temperature along with its index
        for i, temp in enumerate(temperatures):
            # while the stack is not empty and the current temperature is greater than
            # the temperature corresponding to the index at the top of the stack:
            while stack and temp > temperatures[stack[-1]]:
                # pop the index from the stack and calculate the difference with the current index
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            # push the current index onto the stack
            stack.append(i)
        
        # return the result array
        return result

solution = Solution()
temperatures1 = [73,74,75,71,69,72,76,73]
print(solution.dailyTemperatures(temperatures1))

temperatures2 = [30,40,50,60]
print(solution.dailyTemperatures(temperatures2))

temperatures3 = [30,60,90]
print(solution.dailyTemperatures(temperatures3))