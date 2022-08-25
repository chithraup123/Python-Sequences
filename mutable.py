
str = "abc"
print(id(str))
str = "xyz"
print(id(str))

# Mutable object is one whose value can be changed without the objects being destroyed and re-created
# Following are the mutable objects in python
# list
# dict
# set
# ByteArray

# example

shopping_list = ["bread", "cheese", "rice", "eggs", "veggies"]
another_list = shopping_list
print("Id of shopping_list and another_list are: ")
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))  # gives same id, so it shows that we can go to the memory and change the value
# In case of immutable, while changing the value python creates a new object with another id
# and old object keeps the same value

# now print another_list, it gives same value of shopping_list since both are pointed to same object
print(f"another list is {another_list}")

# See the following example
#########################################
a = b = c = d = another_list
shopping_list += ["chocolates"]
print(f"The value inside a is {a}")
# here a is bound to the same object which is assigned for another_list and shopping_list

# modify c and print shopping_list
print("~" * 60)
c.append('Cream')
print(shopping_list)

# modify d and print shopping_list
print("~" * 60)
d.insert(0, "Curd")
print(shopping_list)
