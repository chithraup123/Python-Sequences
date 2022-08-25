# Swapping
list1 = [12, 35, 9, "", 56, 24]

#  method 1
# temp = list1[0]
# list1[0] = list1[len(list1) - 1]
# list1[len(list1) - 1] = temp
# print(list1)

# method 2
# list1[0], list1[-1] = list1[-1], list1[0]
# print(list1)

# method 3
# num_tuple = list1[0], list1[-1]
# print(num_tuple)
# list1[-1], list1[0] = num_tuple
# print(list1)

# method 4
start, *middle, end = list1
list1 = end, *middle, start
# list1 = 'a', 'b', 'c'
print(str(list1))
print(' '.join(map(str, list1)))  # to convert tuple to string

list2 = ["one", "two", "three"]
print(type(list2))
# convert list to tuple method1
tuple_str = tuple(list2)

# convert list to tuple method2
newList2 = (*list2),
print(newList2)
