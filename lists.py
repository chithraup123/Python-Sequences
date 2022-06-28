computer_parts = ["computer", "monitor", "keyboard", "mouse", "cpu"]

for part in computer_parts:
    print(part)  # prints all items in the computer_parts

print("~" * 60)
print(computer_parts[1])

print("~" * 60)
print(computer_parts[-1])

print("~" * 60)
for part in computer_parts[0:4:2]:
    print(part)
################################################################
#  Remove from list
print("Removing mouse from parts\n****************************")
computer_parts.remove("mouse")
for part in computer_parts:
    print(part)
################################################################
#  Extend to a list,
#  extend method takes all items from iterable(sequence) we pass and add to the existing list.

even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print(even)

# len function
# to find the length of the sequence
length = len(odd)
print(length)
print(str(odd[0]))
print(type(odd[0]))
#######################################################
# How to create list
empty_list = []  # create empty list
alphabets = "pqrabcxyz"
alpha_list = list(alphabets)  # create list from a sequence
print(alpha_list)
copy_alphabets = alpha_list.copy()  # create string by copying the list variable
#  Copy the list to another variable
new_list = []
for item in alpha_list:
    new_list.append(item)
print(new_list)
print(alpha_list is new_list)  # check whether aplha_list and new_list points to the same object
print(alpha_list == new_list)  # check whether the items are equal

# else import copy and use .copy method
###########################################################

str1 = "abcdef"
# str1[-1] = "g"  # error since string is immutable
print(str1[-1])

# Replace item in a list

computer_parts.append("mouse pad")
computer_parts.append("headset")
print(computer_parts)
# replace 3rd and 4th item by some other item
computer_parts[4:] = "mouse"
#  list item/slice can't be replaced with string variable, first we need to convert it into list
print(computer_parts)

# convert it into list and replace from 4th item to mouse list
computer_parts[4:] = ["mouse"]
print(computer_parts)
#########################################################
# Delete data from list
data = [4, 3, 6, 8, 9, 12, 56, 43]
print(data)
del data[1:3]  # del uses to delete items from list
print(data)
# how to remove data safely
#  Following is the unsorted list of numbers where we want to remove <10 and >50 numbers
# 1. Sort it first
# 2. Removes the items < 10 first
data = [4, 12, 6, 15, 9, 12, 56, 43, 10, 38, 79, 29, 22]
data.sort()
print(f"After sorting.......\n{data}")

stop = 0
for index, value in enumerate(data):
    if value > 10:
        stop = index - 1
        break
print(stop)
del data[:stop]
print(data)

# 3. Then remove items > 10
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= 10:  # if 10 is found, then start can be moved one step forward to 10
        # so that 10 will not get removed
        start = index + 1
        break
del data[start:]
print(data)
#######################################################################################
data = [4, 12, 6, 15, 9, 12, 56, 43, 10, 38, 79, 29, 22]

######################################################
#  Simple code for removing <10 and >10 values
data.sort()
print(f"After sorting.......\n{data}")
for index in range(len(data) - 1, -1, -1):
    if data[index] > 10 or data[index] < 10:
        print(index)
        del data[index]
print(data)
