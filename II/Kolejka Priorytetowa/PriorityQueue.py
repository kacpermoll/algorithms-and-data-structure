import numpy as np


class PriorityQueue:
    def __init__(self, MAX_SIZE):
        self.MAX_SIZE = MAX_SIZE
        self.tail = -1
        self.head = -1
        self.array = [-np.inf] * MAX_SIZE

    def add(self, value):
        if (self.head <= 1 and self.tail == self.MAX_SIZE - 1) or (
            self.tail == self.head - 2
        ):
            return print("Adding is impossible, the queue is full!")

        # we have to change index of head
        # in the result of adding an element to the empty queue
        if self.head == -1:
            self.head = 0

        # tail is in the end of the queue
        # instead of moving tail one position to the left
        # move it to the begining and save there
        if self.tail == self.MAX_SIZE - 1:
            self.tail = 0
            self.array[self.tail] = value
            return

        self.tail += 1
        self.array[self.tail] = value

    def remove(self):
        if self.head == -1 and self.tail == -1:
            return print("Removing is impossible, the queue is empty!")

        # finding the greatest value and index of it
        max = self.array[self.head]
        index_of_max = self.head
        for i in range(len(self.array)):
            if self.array[i] > max:
                max = self.array[i]
                index_of_max = i

        # changing head and max
        self.array[self.head], self.array[index_of_max] = (
            self.array[index_of_max],
            self.array[self.head],
        )

        pop_value = self.array[self.head]
        self.array[self.head] = -np.inf

        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return

        if self.head == self.MAX_SIZE - 1:
            self.head = 0
        else:
            self.head += 1

        return pop_value

    def find(self, value):
        for n in range(len(self.array)):
            if value == self.array[n]:
                return n


first = PriorityQueue(3)

run = True
while run:
    choice = int(
        input(
            "Choose what would you like to do: \n 1. Enqueue \n 2. Dequeue"
            + "\n 3. Find by value\n 4. Exit\n "
        )
    )
    if choice == 1:
        number = int(input("Enter a value to enqueue: "))
        first.add(number)
    elif choice == 2:
        first.remove()
    elif choice == 3:
        number = input("Enter value which you are looking for:")
        if type(first.find(number)) is int:
            print(f"It is on the {first.find(number)+1} position")
        else:
            print("There is no such a value")

    elif choice == 4:
        run = False

    print(first.array)
    print(f"Tail: {first.tail}")
    print("")
