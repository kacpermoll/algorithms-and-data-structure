import time
import random


def mergeSort(arr):

    # if an array has more than one element
    if len(arr)-1 > 0:

        # assigning the middle element to the variable mid
        mid = len(arr)//2

        # dividing an array into two parts using the middle element
        L = arr[:mid]
        R = arr[mid:]

        # recursive execution of functions for both parts of the array
        mergeSort(L)
        mergeSort(R)

        # merging an array using the merge function
        merge(arr, L, R)


def merge(arr, L, R):

    i = j = k = 0

    # as long as L and R have elements
    # sorting takes place, the smaller element is written into the arr array
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            k += 1
            i += 1
        else:
            arr[k] = R[j]
            k += 1
            j += 1

    # if there are any elements left in any of the arrays, they should be added to arr
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def main():
    tab = [random.randint(0, 100) for i in range(100000)]
    # print("Przed sortowaniem:")
    # print(tab)
    start_time = time.time()
    mergeSort(tab)
    print("--- %s seconds ---" % round(time.time() - start_time, 10))
    # print("Po:")
    # print(tab)


if __name__ == '__main__':
    main()
