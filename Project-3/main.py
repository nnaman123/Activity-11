#Diamond Pattern
#take input
rowSize = int(input("Enter the number of rows: "))
if rowSize % 2 == 0: #conditions
    halfDiamRow = int(rowSize / 2)
else:
    halfDiamRow = int((rowSize + 1) / 2)

space = halfDiamRow - 1
#loop for upper half of diamond
for i in range(1, halfDiamRow + 1):
    for j in range(space):
        print(" ", end="")
    num = 1
    for j in range(2 * i - 1):
        print(num, end="")
        num = num + 1
    print()
    space = space - 1

space = 1
#loop for lower half of diamond
for i in range(halfDiamRow - 1, 0, -1):
    for j in range(space):
        print(" ", end="")
    num = 1
    for j in range(2 * i - 1):
        print(num, end="")
        num = num + 1
    print()
    space = space + 1

