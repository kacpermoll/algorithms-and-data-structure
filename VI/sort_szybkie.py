def QuickSort(T):
    if len(T) <= 1:
        return T
    else:
        pivot = T[0]
        less = [i for i in T[1:] if i <= pivot]
        greater = [i for i in T[1:] if i > pivot]
        return QuickSort(less) + [pivot] + QuickSort(greater)
