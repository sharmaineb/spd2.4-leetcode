"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
"""

# calculate the total sum of all the elements in array
# initialize a variable left_sum to 0 to track the sum of elements to the left of the current index
# iterate through each element in the array
# for each index i check if left_sum is equal to the total sum minus the left_sum and element at index i
# if it is, return i as the pivot index
# otherwise, add the current element to left_sum
# if no pivot index is found during iteration, return -1 to indicate that no pivot index exists

class Solution:
    def pivotIndex(self, nums):
        # calculate the total sum of all the elements in array
        total_sum = sum(nums)
        # initialize a variable left_sum to 0 to track the sum of elements to the left of the current index
        left_sum = 0
        # iterate through each element in the array
        for i in range(len(nums)):
        # for each index i check if left_sum is equal to the total sum minus the left_sum and element at index i
            if left_sum == total_sum - left_sum - nums[i]:
                # if it is, return i as the pivot index
                return i
            # otherwise, add the current element to left_sum
            left_sum += nums[i]
        # if no pivot index is found, return -1
        return -1

sol = Solution()

nums1 = [1,7,3,6,5,6]

print(sol.pivotIndex(nums1))