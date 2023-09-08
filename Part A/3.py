## Write a Python program to construct the following pattern, using a nested for-loop.
## *
## * *
## * * *
## * * 
## *

for i in range(0, 3):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(3, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()