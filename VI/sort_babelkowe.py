def bubblesort(T):
    for i in range(0, len(T)):
        for j in range(0, len(T)-i-1):
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]


T = [12, 11, 13, 5, 6]
bubblesort(T)
print("Sorted array is: ")
print(*T, sep="*")
