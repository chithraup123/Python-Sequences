print('Please enter three numbers: ')
inputStr = input()
a, b, c = inputStr.split(',')
calc = int(a) + int(b) - int(c)
print(calc)