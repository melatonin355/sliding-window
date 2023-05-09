'''
Write a function longest_substring_k_distinct that takes a string and a positive integer 'k' as inputs, and returns the length of the longest substring in it with no more than 'k' distinct characters. The function should be efficient in terms of time complexity.

Example:

assert longest_substring_k_distinct("araaci", 2) == 4

Problem Constraints:
The input string 's' will only contain lowercase English letters.
The length of the input string 's' will be greater than 0.
The input 'k' will be a positive integer.
Your function should return the length of the longest substring in the input string with no more than 'k' distinct characters.
Function Signature:
start 
letter counter: dict
expand by iterating:
  add to a letter count for eack occurence
  while len of letter count is greater than k:
    subtract one from the letter count for the leetter at the start pos.
    if letter counter[s[start]] is 0:
      delete letter counter [s[start]]
    add one to start pointer.

 del mydict[something]
'''

from collections import defaultdict
# ("araaci", 2)
def longest_substring_k_distinct(s, k):
    letter_count = defaultdict(int)
  # {c: 1, i: 1}
    start = 0 # 1
    max_substring = 0 #4
    for end in range(len(s)):
      letter_count[s[end]] +=1
      while len(letter_count) > k:
        letter_count[s[start]] -= 1
        if letter_count[s[start]] == 0:
          del letter_count[s[start]]
        start += 1
      max_substring = max(max_substring, sum(letter_count.values()))
    return max_substring


assert longest_substring_k_distinct("araaci", 1) == 2
assert longest_substring_k_distinct("cbbebi", 3) == 5
assert longest_substring_k_distinct("abcabcabc", 2) == 2
assert longest_substring_k_distinct("aaaaaa", 1) == 6


'''
mydict = {}
mydict["nolan"] = 1

print(mydict)

del mydict["nolan"]

print(mydict)
'''
