def MergeSort(arr):
    
    if len(arr) > 1:
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        MergeSort(left)
        MergeSort(right)

        Merge(arr, left, right)

def Merge(arr, left, right):
    
    length = len(left) + len(right)

    i = 0
    j = 0
    k = 0

    #Shift the smaller value
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1

    #Finish left array if right is shorter
    while i < len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    #Finish right array if left is shorter
    while j < len(right):
        arr[k] = right[j]
        j+=1
        k+=1

    
lst = [5,2,10,1,8,-3]
print(lst)
MergeSort(lst)
print(lst)

