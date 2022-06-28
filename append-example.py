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

data =[10, 5, 20, 30, 25, 15]
for index, value in enumerate(reversed(data)):
    print(index, value)

