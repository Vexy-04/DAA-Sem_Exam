# Write a Python program to display Fibonacci series for the given number.

def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))


num = int(input("Enter the number upto which series should be printed: "))
if num <= 0:
    print("Please enter a Positive Number")
else:
    print("Fibonacci Series:", end=" ")
for i in range(num):
    print(fibonacciSeries(i), end=" ")

# Enter the number upto which series should be printed: 10
# Fibonacci Series: 0 1 1 2 3 5 8 13 21 34
