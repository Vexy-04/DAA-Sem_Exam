# Write a Python program to find the greatest common divisor (gcd) of two integers.

n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))
ans = 0
if n > m:
    for i in range(1, n):
        if n % i == 0 and m % i == 0:
            ans = i
else:
    for i in range(1, m):
        if n % i == 0 and m % i == 0:
            ans = i
print("The GCD of", n, "and", m, "is", ans)

# Enter the first number: 48
# Enter the second number: 60
# The GCD of 48 and 60 is 12
