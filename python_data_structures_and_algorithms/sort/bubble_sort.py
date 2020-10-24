'''
* Sắp xếp nổi bọt
'''


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [64, 34, 25, 23, 11, 90]
print('=== Bubble Sort ===')
print('first: ', arr)
bubble_sort(arr)
print('sort: ', arr)
