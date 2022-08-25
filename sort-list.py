#  Sort a list, cann
#  Sort method here doesn't create the copy of the list, just rearranges the list
# is a method available in list class, so it can be used only with list variable

even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
even.sort()  # doesn't return anything(returns None), so we cannot assign this to another variable
print(even)

#  Sort in reverse order/descending order
even.sort(reverse=True)
print(even)

numList = ["x", "y", "a", "c", "w"]
numList.sort(reverse=True)
print(numList)
##############################################################
pangram = "The quick brown fox jumps over the lazy dog"
#  Sorted function takes any iterable and returns a list in ascending/alphabetical order
# but uppercase letters sort before lowercase
# also duplicated items will not get removed here
letters = sorted(pangram)
print(f"The result of sorted function is {letters}")

even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
sorted_numbers = sorted(even)  # returns sorted list
#  comparing to sort method, sorted function returns a new list and left the original list unchanged
#  so 2 list variables need to be used here
print(sorted_numbers)

#  How to avoid uppercase letters while sorting
###################################################
# for both sort and sorted methods this cane be used to avoid considering capital case while sorting
letters = sorted(pangram, key=str.casefold)
print(letters)

str1 = ["z", "g", "e", "a", "C"]
str1.sort(key=str.casefold)
print(str1)
str1.sort(key=str.casefold, reverse=True)
print(str1)

digits = sorted("4329856")
print(digits)
