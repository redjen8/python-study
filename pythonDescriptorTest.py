class Queue:
    by = 0

    def __init__(self, num):
        self.lst = []

    def enQueue(self, num):
        self.lst.append(num)

    def deQueue(self):
        if len(self.lst) == 0:
            return -1
        else:
            return self.lst.pop(0)

    def byAdd(self, num):
        self.by += num


Qlist = [Queue(i) for i in range(0, 10)]

for n, Q in enumerate(Qlist):
    print(n, hex(id(Q.lst)), hex(id(Q.by)))

Qlist[0].enQueue(2)
Qlist[1].enQueue(3)

for i in range(5):
    print(Qlist[i].lst)

Qlist[0].byAdd(100)
for i in range(5):
    print(Qlist[i].by)

for n, Q in enumerate(Qlist):
    print(n, hex(id(Q.lst)), hex(id(Q.by)))
