#Author: Robert Davis

def HeapSort(arr):

    lst = [0]*len(arr)

    count = len(arr) - 1

    while count >= 0:
        BuildHeap(arr)
        lst[count] = arr[0]
        arr = arr[1:]
        count-=1

    return lst

def BuildHeap(arr):

    pos = len(arr)//2

    while pos >= 0:
        MaxHeapPos(arr, pos)
        pos-=1
    

def MaxHeapPos(arr, pos):

    left = 2*pos + 1
    right = 2 * pos + 2
    largest = pos

    if left < len(arr) and arr[left] > arr[largest]:
        largest = left
    if right < len(arr) and arr[right] > arr[largest]:
        largest = right
    if largest != pos:
        arr[pos], arr[largest] = arr[largest], arr[pos]
        MaxHeapPos(arr, largest)

    
lst = [5,1,2,7,6,14,8,9]
print(lst)

print(HeapSort(lst))

print(lst)
