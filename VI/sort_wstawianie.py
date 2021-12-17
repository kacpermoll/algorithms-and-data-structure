import time
import random


def insertionSort(T):

    for k in range(1, len(T)):

        temp = T[k]

        j = k-1

        while j >= 0 and temp < T[j]:
            T[j+1] = T[j]
            j -= 1

        T[j+1] = temp


def main():
    tab = [random.randint(0, 100) for i in range(100000)]
    # print("Przed sortowaniem:")
    # print(tab)
    start_time = time.time()
    insertionSort(tab)
    print("--- %s seconds ---" % round(time.time() - start_time, 10))
    # print("Po:")
    # print(tab)


if __name__ == '__main__':
    main()
