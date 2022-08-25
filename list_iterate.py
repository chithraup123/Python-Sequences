# Remove negative values
# sleep_durations = [268, -590, -326, 506]
# for val in sleep_durations[:]:
#     if val < 0:
#         sleep_durations.remove(val)
# print(sleep_durations)


def print_multiples(n, maximum):
    for i in range(n, maximum + 1):
        if i % n == 0:
            print(i)


print_multiples(4, 10)
