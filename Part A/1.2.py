## Write a Python program to create an array of 5 integers and display the array items. Access individual elements through indexes.

array = [int(x) for x in input("Enter the elements of the array, separated by spaces: ").split()]
print("The array elements are: ",array)

if __name__ == "__main__":
    while True:
        index = int(input("Enter the index: "))
        if index < len(array):
            print("Element at index", index, "is:", array[index])
        else:
            print("Invalid index!")
        try_again = input("Do you want to try again with different number (y/n):").lower()
        if try_again != "y":
            break
'''
Enter the elements of the array, separated by spaces: 10 20 30 40 50
The array elements are:  [10, 20, 30, 40, 50]
Enter the index: 0
Element at index 0 is: 10
Invalid index!
Do you want to try again with different number (yes/no):no
'''