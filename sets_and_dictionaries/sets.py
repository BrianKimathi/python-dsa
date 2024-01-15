my_set = {1, 2, 3}

my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

my_set.discard(3)
print(my_set)  # Output: {1, 4}

popped_value = my_set.pop()
print(popped_value)  # Output: 1

my_set.clear()
print(my_set)  # Output: set()

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}