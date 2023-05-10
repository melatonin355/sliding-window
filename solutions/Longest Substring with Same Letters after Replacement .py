"""
Longest Substring with Same Letters after Replacement 
Problem Statement
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2  
Output: 5  
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1  
Output: 4  
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1  
Output: 3  
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
Try it yourself
Try solving this question here:
"""
'''
dict: letter frequency
most common letter: max(dict)
start: 0

'''
#from collections  

def length_of_longest_substring(str1, k):
  max_length = 0
  start = 0 
  frequency = {} 
  most_common_letter = 0
  # "abbcb"
  for end in range(len(str1)):
    if str1[end] not in frequency: 
      frequency[str1[end]] = 0
			
    frequency[str1[end]] += 1
    most_common_letter = max(frequency.values())
    window_size = end - start + 1
    minimum_change = window_size - most_common_letter
    while minimum_change > k:
      frequency[str1[start]] -= 1
      start += 1
      most_common_letter = max(frequency.values())
      window_size = end - start + 1
      minimum_change = window_size - most_common_letter
    
    max_length = max(max_length, window_size)
  # TODO: Write your code here
  return max_length






print(length_of_longest_substring("aabccbb", 2))
print(length_of_longest_substring("abbcb", 1))
print(length_of_longest_substring("abccde", 1))


"""
frequency = {}
frequency["a"] =1
# a -> 1 
# b -> 0
print(frequency["a"]) 
print(frequency["b"]) # -> 0
frequency.get("b", 0)
"""

