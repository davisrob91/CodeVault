#Author: Robert Davis

def CountingSort(arr, max_value):
    """ Returns an array of sorted integer values. This function is most
    efficient when there is a limited variety of values. """

    counted_lst = [0] * (max_value + 1)

    for x in arr:
        counted_lst[x]+=1

    lst = []
    for num, x in enumerate(counted_lst):
        while x > 0:
            lst.append(num)
            x-=1
    return lst

lst = [5,1,0,5,0,3,0,1]
print(CountingSort(lst, 5))

        
