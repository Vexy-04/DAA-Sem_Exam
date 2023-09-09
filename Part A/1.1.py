## Write a Python program to create an array of 5 integers and display the array items. Access individual elements through indexes.

# Create an array of 5 integers
array = [int(x) for x in input("Enter the elements of the array, separated by spaces: ").split()]

# Display the array items
print("Array items:")
for i in range(len(array)):
    print(f"Element at index {i}: {array[i]}")

# Array items:
# Element at index 0: 10
# Element at index 1: 20
# Element at index 2: 30
# Element at index 3: 40
# Element at index 4: 50