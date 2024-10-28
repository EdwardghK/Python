def bubble_sort(arr):
    indexing_length = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(indexing_length):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

original_array = [5, 3, 6, 5, 9, 1, 2, 5, 3, 6, 7, 8, 9, 3]
print("Original array:", original_array)
sorted_array = bubble_sort(original_array.copy())
print("Sorted array:", sorted_array)
