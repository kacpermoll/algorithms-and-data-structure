def QuickSort(T):
    if len(T) <= 1:
        return T
    else:
        pivot = T[0]
        less = [i for i in T[1:] if i <= pivot]
        greater = [i for i in T[1:] if i > pivot]
        return QuickSort(less) + [pivot] + QuickSort(greater)


def main():
    tab = [4, 9, 12, 2, 1, 7, 16, 3]
    print("Przed sortowaniem:")
    print(tab)
    QuickSort(tab)
    print("Po:")
    print(tab)


if __name__ == '__main__':
    main()
