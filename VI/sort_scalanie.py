def mergeSort(T):

    mid = len(T)//2

    L = T[:mid]
    R = T[mid:]

    mergeSort(L)
    mergeSort(R)

    merge(T, L, R)


def merge(T, L, R):
