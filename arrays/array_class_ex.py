# create an array class for which:
# adds an item to an array (list) - insert
# removes items at given index - removeAt
# give index of the first occurrence of an item - indexOf


class ArrayClass:
    def __init__(self):
        self.lst = []

    def insert(self, item):
        self.lst.append(item)

    def remove_at(self, index):
        if index >= len(self.lst):
            raise ValueError(
                f"index must be in the acceptable range (0 - {len(self.lst)})"
            )
        self.lst = [item for i, item in enumerate(self.lst) if i != index]

    def indexOf(self, item_to_find):
        for i, item in enumerate(self.lst):
            if item == item_to_find:
                return i
        return -1

    def maximum(self):
        return max(self.lst)

    def common_item(self):
        test_list = [30, 23, 5, 80]
        result = set(self.lst).intersection(test_list)
        return list(result)

    def rev(self):
        return list(reversed(self.lst))

    def insertAtIndex(self, item, index):
        self.lst.insert(item, index)

    def print(self):
        for item in self.lst:
            print(item)


array = ArrayClass()
array.insert(23)
array.insert(20)
array.insert(80)
array.insert(30)
array.insertAtIndex(2, "HI")
array.print()
