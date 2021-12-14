
def insertionSort(T):

    for k in range(1, len(T)):

        temp = T[k]

        j = k-1

        while j >= 0 and temp < T[j]:
            T[j+1] = T[j]
            j -= 1

        T[j+1] = temp


T = [12, 11, 13, 5, 6]

insertionSort(T)
print("Sorted array is: ")
print(*T, sep="*")
