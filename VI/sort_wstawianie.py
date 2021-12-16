
def insertionSort(T):

    for k in range(1, len(T)):

        temp = T[k]

        j = k-1

        while j >= 0 and temp < T[j]:
            T[j+1] = T[j]
            j -= 1

        T[j+1] = temp


def main():
    tab = [4, 9, 12, 2, 1, 7, 16, 3]
    print("Przed sortowaniem:")
    print(tab)
    insertionSort(tab)
    print("Po:")
    print(tab)


if __name__ == '__main__':
    main()
