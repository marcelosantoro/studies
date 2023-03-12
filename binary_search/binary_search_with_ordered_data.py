def binary_search(data, target):
    """
    Binary Search implementation - Python
    Returns the index of the target value in the list, or None if the value is not found.
    """
    left = 0
    right = len(data) - 1

    while left <= right:
        middle = (left + right) // 2
        if data[middle] == target:
            return middle
        elif data[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return None


"""
Main Program
"""
if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13]
    target = 13

    index = binary_search(data, target)

    if index is not None:
        print(f"Target value {target} was found in index {index} from data list")
    else:
        print(f"Target value {target} was not found in data list")