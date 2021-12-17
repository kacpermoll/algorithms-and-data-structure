import time
import random


def QuickSort(T):
    if len(T) <= 1:
        return T
    else:
        pivot = T[0]
        less = [i for i in T[1:] if i <= pivot]
        greater = [i for i in T[1:] if i > pivot]
        return QuickSort(less) + [pivot] + QuickSort(greater)


def main():
    tab = [random.randint(0, 100) for i in range(100000)]
    # print("Przed sortowaniem:")
    # print(tab)
    start_time = time.time()
    QuickSort(tab)
    print("--- %s seconds ---" % round(time.time() - start_time, 10))
    # print("Po:")
    # print(tab)


if __name__ == '__main__':
    main()
