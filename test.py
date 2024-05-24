class stack:
    def __init__(self):
        self.list = []
    def pop(self):
        if(self.isEmpty()):
            return -1
        x = self.list[-1]
        self.list.pop()
        return x
    def push(self, nr):
        self.list.append(nr)
    def top(self):
        if(self.isEmpty()):
            print("Stack is empty")
            return -1
        return self.list[-1]
    def isEmpty(self):
        if len(self.list) == 0:
            return 1


def copyStiva(stiva, copieStiva):
    for x in stiva.list:
        copieStiva.list.append(x)
stiva1 = stack()
stiva1.push(5)
stiva2 = stiva1
print(stiva2.top())
stiva1.push(10)
print(stiva2.top())
