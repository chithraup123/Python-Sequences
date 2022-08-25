arr = [[1, 2, 3, 4],
       [4, 5, 6, 5],
       [7, 8, 9, 4],
       [6, 3, 2, 7]]

#print(arr[0])
n = len(arr[0])
print(n)

i = 0
for j in range(0, n-1):
    print(arr[i][j], end=" ")

k = 1
for i in range(0, n):
    for j in range(n, 0, -1):
        if (j == n - k):
            print(arr[i][j], end=" ")
            break;
    k += 1

# # Print last row
# i = n - 1;
# for j in range(0, n):
#     print(arr[i][j], end=" ")
