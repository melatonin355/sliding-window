# Prompts Index

1. [Problem 2 - Smallest Subarray with a Greater Sum](#problem-2---smallest-subarray-with-a-greater-sum)
2. [Problem 3 - Longest Substring with K Distinct Characters](#problem-3---longest-substring-with-k-distinct-characters)
3. [Problem 4 - Fruits into Baskets](#problem-4---fruits-into-baskets)
4. [Problem 5 - Longest Substring with Distinct Characters](#problem-5---longest-substring-with-distinct-characters)

---

## [Problem 2 - Smallest Subarray with a Greater Sum](#prompts-index)

Write a function `smallest_subarray_greater_sum` that takes an array of positive numbers and a positive number 'S' as inputs, and returns the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. If no such subarray exists, return 0. The function should be efficient in terms of time complexity.

**Example:**

```python
assert smallest_subarray_greater_sum([2, 1, 5, 2, 3, 2], 7) == 2
```

**Problem Constraints:**

1. The input array 'arr' will only contain positive integers.
2. The length of the input array 'arr' will be greater than 0.
3. The input 'S' will be a positive integer.
4. Your function should return the length of the smallest contiguous subarray whose sum is greater than or equal to 'S', or 0 if no such subarray exists.

**Function Signature:**
```python
def smallest_subarray_greater_sum(arr, S):
    pass
```

**Additional Test Cases:**

```python
assert smallest_subarray_greater_sum([2, 3, 1, 2, 4, 3], 7) == 2
assert smallest_subarray_greater_sum([1, 4, 4], 4) == 1
assert smallest_subarray_greater_sum([5, 1, 2, 3, 1, 6], 12) == 3
assert smallest_subarray_greater_sum([1, 1, 1, 1, 1, 1, 1], 10) == 0
```

---

## [Problem 3 - Longest Substring with K Distinct Characters](#prompts-index)

Write a function `longest_substring_k_distinct` that takes a string and a positive integer 'k' as inputs, and returns the length of the longest substring in it with no more than 'k' distinct characters. The function should be efficient in terms of time complexity.

**Example:**

```python
assert longest_substring_k_distinct("araaci", 2) == 4
```

**Problem Constraints:**

1. The input string 's' will only contain lowercase English letters.
2. The length of the input string 's' will be greater than 0.
3. The input 'k' will be a positive integer.
4. Your function should return the length of the longest substring in the input string with no more than 'k' distinct characters.

**Function Signature:**
```python
def longest_substring_k_distinct(s, k):
    pass
```

**Additional Test Cases:**

```python
assert longest_substring_k_distinct("araaci", 1) == 2
assert longest_substring_k_distinct("cbbebi", 3) == 5
assert longest_substring_k_distinct("abcabcabc", 2) == 2
assert longest_substring_k_distinct("aaaaaa", 1) == 6
```

---
## [Problem 4 - Fruits into Baskets](#prompts-index)


Prompt:
Write a function `max_fruits_in_baskets` that takes a list of characters representing fruit trees as input and returns the maximum number of fruits you can pick according to the given constraints. The function should be efficient in terms of time complexity.


Example:

```python
assert max_fruits_in_baskets(['A', 'B', 'C', 'A', 'C']) == 3
```

**Problem Constraints:**

1. The input list 'fruit' will only contain uppercase English letters.
2. The length of the input list 'fruit' will be greater than 0.
3. Each basket can have only one type of fruit (with no limit to the number of fruit).
4. Start with any tree, but you can't skip a tree once you have started.
5. Pick exactly one fruit from every tree until you cannot. For example, stop when you have to pick from a third fruit type.
6. Your function should return the maximum number of fruits you can pick according to the given constraints.


```python
def max_fruits_in_baskets(fruit: List[str]) -> int:
    pass
```

**Additional Test Cases:**

```python
assert max_fruits_in_baskets(['A', 'B', 'C', 'B', 'B', 'C']) == 5
assert max_fruits_in_baskets(['A', 'A', 'A', 'B', 'C', 'B', 'B', 'A', 'C']) == 5
assert max_fruits_in_baskets(['A', 'B', 'A', 'A', 'B']) == 5
assert max_fruits_in_baskets(['A', 'A', 'A', 'A', 'A']) == 5
```
---


## [Problem 5 - Longest Substring with Distinct Characters](#prompts-index)

Write a function `longest_substring_distinct` that takes a string as input and returns the length of the longest substring in it with all distinct characters. The function should be efficient in terms of time complexity.

**Example:**

```python
assert longest_substring_distinct("aabccbb") == 3
```

**Problem Constraints:**

1. The input string 's' will only contain lowercase English letters.
2. The length of the input string 's' will be greater than 0.
3. Your function should return the length of the longest substring in the input string with all distinct characters.

**Function Signature:**
```python
def longest_substring_distinct(s):
    pass
```

**Additional Test Cases:**

```python
assert longest_substring_distinct("abccde") == 3
assert longest_substring_distinct("bbbbb") == 1
assert longest_substring_distinct("pwwkew") == 3
assert longest_substring_distinct("abcabcbb") == 3
```
