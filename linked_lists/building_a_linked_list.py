"""
Exercise in building linked lists
"""

# _list = []

# _list.append(10)
# _list.append(20)
# _list.append(30)
# _list.insert(0, 5)
# _list.pop()
# print(_list)


# write a class for manipulating lists
# Method names:
# addFirst
# addLast
# deleteFirst
# deleteLast
# contains
# indexOf


class LinkedList:
    "class for manipulating lists"

    def __init__(self):
        self._list = []

    def add_first(self, num):
        "add to front of list"
        self._list.insert(0, num)

    def add_last(self, num):
        "adds to end of list"
        self._list.append(num)

    def print_list(self):
        "prints list"
        print(self._list)


_list = LinkedList()
_list.add_first(5)
_list.add_last(10)
_list.print_list()
