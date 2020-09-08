# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class IntList:

    def __init__(self, f, r):
        self.first = f
        self.rest = r

    def recursivesize(self):
        if self.rest is None:
            return 1
        else:
            return 1 + self.rest.size()
   
    def notrecursive(self):
        pointer = self
        total_size = 0
        while pointer is not None:
            total_size += 1
            pointer = pointer.rest
        return total_size

l = IntList(5, None)
l = IntList(10, l)
l = IntList(15, l)

print(l.size())