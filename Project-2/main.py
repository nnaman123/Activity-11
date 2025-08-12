#floyd's triangle pattern
#take input
rows = int(input("Enter the number of rows: "))
number = 1 #initialize by 1

print("Floyd's triangle ")
#outer loop for number of rows
for i in range(1, rows + 1):
    #inner loop for number of columns
    for j in range(1, i + 1):
        #display result
        print(number, end=" ")
        number = number + 1
    print()