# 1. Find the Largest Element in an Array
arr = [12, 45, 7, 89, 23]
largest = arr[0]
for num in arr:
    if num > largest:
        largest = num
print("Largest element:", largest)
# 2. Find the Smallest Element in an Array
arr = [12, 45, 7, 89, 23]
smallest = arr[0]
for num in arr:
    if num < smallest:
        smallest = num
print("Smallest element:", smallest)
# 3. Reverse an Array
arr = [12, 45, 7, 89, 23]
reversed_arr = arr[::-1]
print("Reversed array:", reversed_arr)
# output:
# Largest element: 89
# Smallest element: 7
# Reversed array: [23, 89, 7, 45, 12]