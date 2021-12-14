
def mergeSort(T):

    if len(T) > 1:
        # finding the mid of the array
        mid = len(T)//2

        # dividing the array elements
        # into 2 halves
        l = T[:mid]
        r = T[mid:]

        # sorting the first half
        mergeSort(l)

        # sorting the second half
        mergeSort(r)

        i = j = k = 0

        # copy data to temp arrays L[] and R[]
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                T[k] = l[i]
                i += 1
            else:
                T[k] = r[j]
                j += 1

            k += 1

            # checking if any element we left
            while i < len(l):
                T[k] = l[i]

        mergeSort(T, l, mid)
        mergeSort(T, mid+1, r)
        merge(T, l, mid, r)


def merge(T, l, mid, r):
    q1 = []
    q2 = []

    for i in range(l, mid):
        q1.append(T[i])

    for i in range(mid+1, r):
        q2.append(T[i])

    q1 = q1.reverse()
    q2 = q2.reverse()

    i = l

    print(q1, q2)


T = (1, 3, 4, 2, 5)
merge(T, 0, 3, len(T))
