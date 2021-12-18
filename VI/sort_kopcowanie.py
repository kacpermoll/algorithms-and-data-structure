import time
import random
from heapq import heappush, heappop


def HeapSort(T):
    heap = []
    for value in T:
        heappush(heap, value)
    return [heappop(heap) for i in range(len(heap))]


def main():
    tab = [random.randint(0, 100) for i in range(100000)]
    # print("Przed sortowaniem:")
    # print(tab)
    start_time = time.time()
    tab = HeapSort(tab)
    print("--- %s seconds ---" % (round(time.time() - start_time, 10)))
    # print("Po:")
    # print(tab)


if __name__ == '__main__':
    main()
