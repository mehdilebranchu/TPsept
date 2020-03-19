class node:
    def __init__(self,d,b):
        self._data = d
        self._nextNode = b

    def getData(self):
        return self._data

    def getNextNode(self):
        return self._nextNode

    def setData(self,a):
        self._data = a

    def setNextNode(self,b):
        self._nextNode = b



obj = node(5,8)
print(obj)

