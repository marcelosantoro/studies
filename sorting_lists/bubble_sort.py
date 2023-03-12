# We have the same result using this python embebed function: nums.sort()
def bubble_sort(nums):
    # Get the length of the list
    n = len(nums)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                #print(nums)
    return nums

if __name__ == "__main__":
    nums = [50,50,50,70,20,30,90,45,78,21,12,1,3]
    
    # Removing repeated values using set
    nums = list(set(nums))
    
    print(bubble_sort(nums))