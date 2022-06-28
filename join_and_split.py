#  join is a method available in str class
#  join cannot be done for types other than string
meal1 = ["rice", "chapati", "dal", "egg"]
meal2 = ["bread", "sandwich", "veggies", "burger"]
print("|".join(meal1))  # join lists items without square brackets

##################################################################
#  Split method
print("bread and butter".split("and"))  # splits the string and returns the list of strings
print("bread".split())  # split will be done on space by default, always return a list
