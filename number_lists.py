from typing import List

even: List[int] = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

print("even min and max\n*************")
print(min(even))
print(max(even))

print("odd min and max\n*************")
print(min(odd))
print(max(odd))

print("Length\n*************")
print(f"Length of even list is {len(even)}")
print(f"Length of odd list is {len(odd)}")

print("Count of list\n***************")
print(f"The count {2} in even list is {even.count(2)}")

print("mississippi".count("s"))
print("abc".count(""))

txt = "I love apples, apple are my favorite fruit"
print("apple count is ")
x = txt.count("apple", 20, 24)
print(x)
