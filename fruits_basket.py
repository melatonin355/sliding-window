"""
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.

Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']  
Output: 3  
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:
Input: Fruit = ['A', 'B', 'C', 'B', 'B', 'C']  
Output: 5  
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

Example 3: 
INPUT: fruit = [A, B, B, C, B, A, D, E]
basket 1: B
basket 2: C
OUTPUT: 4
Explanation: We can put 3 B in basket 1, and 1 C in basket 2 and the subarray is [B, B, C, B] length(4)

Example 4:
fruit = [A]
output: 1
"""
'''
2 baskets:
  1 type of fruit per basket
  each basket can hold any amount of fruit
There can be any number of fruit tree types


The time complexity of the current implementation of the fruits_basket function is O(N^2), where N is the length of the input array.

This is because the function uses a while loop to iterate through each element in the input array, and for each element, it creates a subarray to check if there are at most two types of fruits in the subarray. The set function is used to count the number of unique fruits in the subarray, which has a time complexity of O(K) where K is the number of unique fruits in the subarray.

Since the while loop iterates N times, and for each iteration, it creates a subarray of size up to N, the time complexity of the function is O(N^2).


'''

# O(N^2)
def fruits_basket(fruit):
	# Edge case
  if len(set(fruit)) <= 2:
    return len(fruit)

  start_index = 0
  end_index = 1
  baskets = []

  while end_index < len(fruit):
    types_of_fruit = fruit[start_index: end_index + 1]
    print("type of fruit: {}", types_of_fruit) 
		
    if len(set(types_of_fruit)) <= 2:
      if len(types_of_fruit)> len(baskets):
        baskets = fruit[start_index: end_index + 1] 
      end_index += 1
    else: 
      start_index += 1
  print(baskets)
  return len(baskets)
  

# Test case 1
fruit = ['A']
assert fruits_basket(fruit) == 1
# Test case 2
fruit = ['A', 'B', 'C', 'A', 'C']
assert fruits_basket(fruit) == 3
# test case 3
fruit = ['A', 'B', 'B', 'C', 'B', 'A', 'D', 'E']
assert fruits_basket(fruit) == 4
