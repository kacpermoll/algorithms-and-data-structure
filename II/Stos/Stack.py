
class Stack:
    def __init__(self, MAX_SIZE):
        self.MAX_SIZE = MAX_SIZE
        self.array = [None] * MAX_SIZE
        self.tail = 0

    def add(self, value):
        if self.tail == self.MAX_SIZE:
            return print("Stack is full!")

        self.array[self.tail] = value

        self.tail += 1
        return

    def remove(self):
        if self.tail == 0:
            return print("Stack is empty!")

        value = 0
        value = self.array[self.tail-1]
        self.array[self.tail-1] = None

        self.tail -= 1

        return int(value)

    def topIndex(self):
        if self.tail == 0:
            return print("Stack is empty!")
        return self.array[self.tail-1]


first = Stack(1)

run = True
while run:
    choice = int(
        input(
            "Choose what would you like to do: \n 1. Push \n 2. Pop"
            + "\n 3. Show top element \n 4. Exit\n "
        )
    )
    if choice == 1:
        number = int(input("Enter a value to enqueue: "))
        first.add(number)
    elif choice == 2:
        removed = first.remove()
        if type(removed) is int:
            print(f"Removed element: {removed}")
    elif choice == 3:
        top = first.topIndex()
        if type(top) is int:
            print(f"On the top of the stack is {top} ")

    elif choice == 4:
        run = False

    print(first.array)
