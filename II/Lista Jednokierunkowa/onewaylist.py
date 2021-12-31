class SingleNode:
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        # if the linked list is empty
        # returns True
        # else
        # return false
        return self.head is None

    def add(self, item):
        """Head adds an element"""
        # create a node that saves the item value
        node = SingleNode(item)

        node.next = self.head
        self.head = node

    def append(self, item):
        """Tail adding elements"""
        # create thhe node that saves the item value
        node = SingleNode(item)

        # check if the linked llist is empty
        if self.is_empty():
            self.head = node
        else:
            cur = self.head

            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def remove(self, item):

        """delete node"""

        cur = self.head
        pre = None

        while cur is not None:

            if cur.item == item:

                # if the first is the deleted node
                if not pre:
                    # turn the head pointer to the latter node
                    # of the head node
                    self.head = cur.next
                else:
                    # the next node of the previous node
                    # of the delete position points to the rear node
                    # of the deleted position
                    pre.next = cur.next
                return
            else:
                # continue to move bacck to the node
                pre = cur
                cur = cur.next
        else:
            raise ValueError("Can not find the item!")

    def find(self, item):
        """If the node exists in the linked list,
        function returns true
        otherwise returns false"""

        cur = self.head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
