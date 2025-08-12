#take input
print("half pyramid pattern of stars (*):")
n = int(input("Enter the number of rows: "))
#outer loop for number of rows
for i in range(n):
    #inner loop for number of columns
    for j in range(i + 1):
        #display result
        print("*", end=" ")
    print()