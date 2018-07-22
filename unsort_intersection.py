import random

def arr_intersection(arr1, arr2, arr3):
    """ This functions takes 3 unsorted arrays and finds the integers
    all the arrays share. """

    x = len(arr1) - 1
    y = len(arr2) - 1
    z = len(arr3) - 1

    intersection = {}
    
    while x | y | z != 0:
        if arr1[x] in intersection:
            intersection[arr1[x]] = intersection[arr1[x]] + 1
        else:
            intersection[arr1[x]] = 1
        if arr2[y] in intersection:
            intersection[arr2[y]] = intersection[arr2[y]] + 1
        else:
            intersection[arr2[y]] = 1
        if arr3[z] in intersection:
            intersection[arr3[z]] = intersection[arr3[z]] + 1
        else:
            intersection[arr3[z]] = 1
        x -= 1
        y -=1
        z-=1

    lst = []
    for key, value in intersection.items():
        if value == 3:
            lst.append(key)
    return lst

arr1 = []
arr2 = []
arr3 = []
for x in range(100000):
    arr1.append(random.randrange(0, 5000))
    arr2.append(random.randrange(0, 5000))
    arr3.append(random.randrange(0, 5000))

arr4 = []

for x in range(100000):
    arr4.append(x)
print(arr_intersection(arr1, arr2, arr3))
print(arr4)
