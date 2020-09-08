class IntList:

    def __init__(self, f, r):
        self.first = f
        self.rest = r

    def get(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest.get(i-1)


l = IntList(5, None)
l = IntList(10, l)
l = IntList(15, l)
l = IntList(20, l)
l = IntList(25, l)


print(l.get(3))
#bilibili   54:17 