import time
import random


def bubbleSort(T):
    for i in range(0, len(T)):
        for j in range(0, len(T)-i-1):
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]


def main():
    tab = [random.randint(0, 100) for i in range(100000)]
    # print("Przed sortowaniem:")
    # print(tab)
    start_time = time.time()
    bubbleSort(tab)
    print("--- %s seconds ---" % round(time.time() - start_time, 10))
    # print("Po:")
    # print(tab)


if __name__ == '__main__':
    main()
