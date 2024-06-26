

# create an array class for which:
# adds an item to an array (list) - insert
# removes items at given index - removeAt
# give index of the first occurence of an item - indexOf

class ArrayClass:
    def __init__(self):
        self.lst = []

        
    def insert(self, item):
        self.lst.append(item)
        
    def removeAt(self, index):
        del self.lst[index]
        
    def indexOf(self, item_to_find):
        return self.lst.index(item_to_find)
        
    
    
array = ArrayClass()
array.insert(10)
array.insert(20)
array.insert(30)

for item in array.lst:
        print(item)

# array.removeAt(1)
print("\n")
# for item in array.lst:
#         print(item)
        
print(array.indexOf(20))