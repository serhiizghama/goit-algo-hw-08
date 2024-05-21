# goit-algo-hw-08

# Task-1
### Cable Connection Cost Minimization

This project provides a Python implementation to minimize the cost of connecting multiple cables using a min-heap (priority queue). The algorithm ensures that the total cost is minimized by always connecting the two shortest cables available.

### Algorithm

The algorithm is based on the following steps:

1. Create a min-heap from the list of cable lengths.
2. While there is more than one cable in the heap:
   - Extract the two shortest cables.
   - Connect these two cables, which incurs a cost equal to the sum of their lengths.
   - Add this cost to a list of costs.
   - Insert the resulting new cable back into the heap.
3. The total cost is the sum of all individual connection costs.

# Task-2

### Merge k Sorted Lists

This project provides a Python implementation to merge `k` sorted linked lists into a single sorted list. The algorithm uses a min-heap (priority queue) to efficiently merge the lists while maintaining the sorted order.

### Algorithm

The algorithm is based on the following steps:

1. Initialize an empty min-heap.
2. Deep copy the input lists to avoid modifying the original lists.
3. Iterate through the copied lists, pushing the first element of each list onto the heap.
4. Pop elements from the heap and append them to the result list.
5. Continue pushing and popping elements until all lists are merged.

