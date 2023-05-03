"""
53. Maximum Subarray Medium

Companies
Given an integer array nums, find the 
*subarray* with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Example 4:
Input: nums = [-1, 2, 4]
Output: 6
Explanation: subarray [2,4] has the largest sum  6 
"""
'''
return only the sum of the subarray
prep for any integer and only integers
'''
'''
create window_start, maxSum 
iterate to expand the window:
    maxSum = max(maxSum, sum(window))
'''

# current_sum = 1
# [-1, 2, 4]
#      L
#      R
def maxSum(nums):
  largest = nums[0]
  current_sum = 0
  window_start = 0
  max_number_so_far = nums[0]

	# Grow window
  for end in range(len(nums)):
    # update current sum
    max_number_so_far = max(max_number_so_far, nums[end])
    current_sum += nums[end] 
    # shrink the window
    if current_sum < 0:
      current_sum = 0
      window_start += 1
    # update the largest
    largest = max(largest, current_sum)
		
  if largest == 0:
    return max_number_so_far
		
  else:
    return largest
      
    

# test case
nums1 = [-1, 2, 4]
assert maxSum(nums1) == 6
nums2 = [5,4,-1,7,8]
assert maxSum(nums2) == 23
nums3 = [-2,1,-3,4,-1,2,1,-5,4]
assert maxSum(nums3) == 6
nums4 = [-2,-1,-3]
assert maxSum(nums4) == -1
