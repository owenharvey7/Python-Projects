"""
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.
Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

Example 1:
Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.

Example 2:
Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.

Constraints: 2 <= nums.length <= 5 * 104
Difficulty: Medium
"""
#Solution
class Solution(object):
    def maxWidthRamp(self, nums):
        # Initialize an empty stack to store indices
        stack = []

        # Step 1: Build a stack of decreasing elements
        for i in range(len(nums)):
            # We only add indices where the current element is less than
            # the element at the top of the stack (to maintain decreasing order)
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        # Initialize variable to store the maximum width of the ramp
        max_width = 0

        # Step 2: Traverse the array from right to left
        for j in range(len(nums) - 1, -1, -1):
            # Try to pop the stack while nums[j] is greater than or equal to nums[stack[-1]]
            # This ensures nums[i] <= nums[j] where i is from the stack and j is the current index
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                max_width = max(max_width, j - i)  # Update the maximum width
        
        # Return the maximum width found
        return max_width
