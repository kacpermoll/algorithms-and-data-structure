def bubbleSort(T):
    for i in range(0, len(T)):
        for j in range(0, len(T)-i-1):
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]


def main():
    tab = [4, 9, 12, 2, 1, 7, 16, 3]
    print("Przed sortowaniem:")
    print(tab)
    bubbleSort(tab)
    print("Po:")
    print(tab)


if __name__ == '__main__':
    main()
