class Stack:
    def __init__(self, MAX_SIZE):
        self.MAX_SIZE = MAX_SIZE
        self.array = [None] * MAX_SIZE

    # returns index of last element
    def topIndex(self):
        i = 0
        if self.array[i] == None:
            return print("Stack is empty!")
        while self.array[i] != None:
            if i < self.MAX_SIZE - 1:
                i += 1
            else:
                return self.MAX_SIZE
        return i - 1

    def remove(self):
        if self.topIndex() == -1:
            print("Stack is empty!")
        else:
            value = self.array[self.topIndex()]
            self.array[self.topIndex()] = None
            return value

    def add(self, value):
        if self.topIndex() == self.MAX_SIZE:  # -1
            print("Stack is full")
        else:
            self.array[self.topIndex() + 1] = value


first = Stack(3)

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
        first.remove()
        if type(first.remove()) is int:
            print(f"Removed element: {first.remove()}")
    elif choice == 3:
        number = input("Enter value which you are looking for:")
        if type(first.topIndex(number)) is int:
            print(f"On the top of the stack is {first.topIndex(number)+1} ")
        else:
            first.topIndex(number)

    elif choice == 4:
        run = False

    print(first.array)
