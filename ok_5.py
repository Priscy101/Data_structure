# Binary Search on Unsorted Array

def binary_search(arr, target):
    # Function to perform binary search on a sorted array
    # It returns the index of the target if found, otherwise -1

    # Sort the array first
    arr.sort()

    # Binary Search
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    # Test the binary search algorithm on an unsorted array

    # Example unsorted array
    unsorted_array = [5, 2, 9, 1, 5, 6, 8, 3]

    # Target element to search for
    target_element = 6

    # Perform binary search
    result = binary_search(unsorted_array, target_element)

    if result != -1:
        print(f"Element {target_element} found at index {result}.")
    else:
        print(f"Element {target_element} not found in the array.")

