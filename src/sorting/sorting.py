# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged = []
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            merged.append(arrA.pop(0))
        else:
            merged.append(arrB.pop(0))
    merged += arrA + arrB
    return merged

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        arrA = merge_sort(arr[:len(arr) // 2]) 
        arrB = merge_sort(arr[len(arr) // 2:])
        return merge(arrA, arrB)
    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    while start < end and start < mid:
        if arr[start] > arr[mid]:
            arr.insert(start, arr.pop(mid))
            start += 1
            mid += 1
        else:
            start += 1
    return arr


def merge_sort_in_place(arr, l, r):
    pass
