from heapq import heapify


def HeapSort(T):
    n = len(T)
    for i in range(n//2 - 1, -1, -1):
        heapify(T, i, n)
    for i in range(n-1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T, 0, i)
    return T


def heapify(T, i, n):
    l = 2*i+1
    r = 2*i+2

    if l < n and T[l] > T[i]:
        largest = r

    if r < n and T[r] > T[l]:
        largest = r

    if largest != i:
        T[i], T[largest] = T[largest], T[i]
        heapify(T, largest, n)
