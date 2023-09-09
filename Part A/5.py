# Write a Python program to demonstrate sequential search.

def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


array = [int(x) for x in input(
    "Enter the elements of the array, separated by spaces: ").split()]
target = int(input("Enter the target element: "))
result = sequential_search(array, target)
if result != -1:
    print("Element", target, "found at index", result)
else:
    print("Element", target, "not found in the array")

# Enter the elements of the array, separated by spaces: 20 10 3 4 52 19
# Enter the target element: 4
# Element 4 found at index 3
