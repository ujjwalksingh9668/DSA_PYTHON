# python code to print the English alphabet "S"...

#Solution:-
n = int(input())
for row in range(n):
    for col in  range(n):
        if row == 0:
            print("*",end=" ")
        elif col == 0 and row <= n // 2:
            print("*",end=" ")
        elif row == n // 2:
            print("*",end=" ")
        elif col == n - 1 and row >= n // 2:
            print("*",end=" ")
        elif row == n - 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
