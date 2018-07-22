def QuickSort(arr, first, last):

    if last > first:
        pivot_pos = last - 1
        pivot = arr[pivot_pos]
        i = first
        
        #Partition (anything smaller than pivot is pushed left)
        for j in range(first, last):
            if arr[j] < pivot:
                arr[i],arr[j] = arr[j], arr[i]
                i+=1

        #Swap pivot point for the first value greater than pivot        
        arr[i], arr[pivot_pos] = arr[pivot_pos], arr[i]

        #Recursively call on left and right halves
        QuickSort(arr, first, i)
        QuickSort(arr, i+1, last)


lst = [5,4,2,10,15, 3, 69, -4, 100, 5]
print(lst)
QuickSort(lst, 0, len(lst))
print(lst)



    
