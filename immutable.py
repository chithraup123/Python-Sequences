#  int, float, str are immutable, we cannot change the value of a 2, 1.67, "hello world" etc
#  examples

result = True  # result has bound to True value
another_result = result
print(id(result))  # gives id of True
print(id(another_result))  # gives id of True, so the previous id and this id will be same

print("~"*60)

result = False  # here result has bound to False value
print(id(result))  # gives id of False

#  So True and False are immutable, while running the program it always gives the same result, we cannot change it
