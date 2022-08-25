# split from the start and add to the end
arr = [12, 10, 5, 6, 52, 36]

print("Enter the position to split from: ")
position = int(input())
split = arr[:position]
new_array = arr[position:len(arr)]+split
print(new_array)
