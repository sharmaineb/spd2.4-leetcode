"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

"""

# iterate through the flowerbed array and check each plot to see if we can plant a flower
        # check each empty plot and its neighboring plot
        # keep track of the count of planted flowers and return True if
        # count is greater than or equal to the required number of new flowers n
        # if we can't plant enough new flowers without violating the no adjacent rule, return False

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed = [0] + flowerbed + [0]
        count = 0
        i = 1

        while i < len(flowerbed) - 1:
            # checks if the current plot and its neighbors are all empty
            if flowerbed[i -1] == flowerbed[i] == flowerbed[i + 1] == 0:
                # plant a flower at the current plot
                flowerbed[i] = 1
                # increment the count of planted flowers
                count += 1
                # skip the next plot since it's adjacent to the current one
                i +=1 
            i +=1

        return count >= n

sol = Solution()
flowerbed1 = [1,0,0,0,1]
n1 = 1

flowerbed2 = [1,0,0,0,1]
n2 = 2

print(sol.canPlaceFlowers(flowerbed1, n1))
print(sol.canPlaceFlowers(flowerbed2, n2))