import math

def smallest_subarray_greater_sum(arr, S): # [1,4,4], 4
    shortest_array = math.inf
    start = 0 # 3
    total = 0
    for end in range(len(arr)):
      total += arr[end] #9
      window_size = end - start + 1 # 3
      while total >= S:
				# only update when the new window size is smaller 
        if window_size == 1:
          return window_size
        elif window_size < shortest_array:# 3
          shortest_array = window_size
        total -= arr[start]
        start += 1
        window_size = end - start + 1
        
          
    if shortest_array == math.inf:
      return 0
    else:
      return shortest_array

