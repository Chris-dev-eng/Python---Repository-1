# 1. Create an empty list
my_list = []
print(f"Empty list: {my_list}")

# 2. Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"After appending elements: {my_list}")

# 3. Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print(f"After inserting 15: {my_list}")

# 4. Extend with [50, 60, 70]
my_list.extend([50, 60, 70])
print(f"After extending: {my_list}")

# 5. Remove the last element
my_list.pop()
print(f"After removing last element: {my_list}")

# 6. Sort in ascending order
my_list.sort()
print(f"After sorting: {my_list}")

# 7. Find index of value 30
index_of_30 = my_list.index(30)
print(f"Index of 30: {index_of_30}")


