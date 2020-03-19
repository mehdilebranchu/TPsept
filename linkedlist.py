from node import *

class linkedlist:
    def __init__(self,r):
        self._root = r
    def addFirst(self,d):
        newNode = node(d, self._root)
        self._root = newNode
        return newNode
    def addLast(self,d):
        newNode = node(d, None)
        current = self._root
        while current.getNextNode() is not None:
            current = current.getNextNode()
        current.setNextNode(newNode)
    def addAfter(self, prevNode, d):
        current =self._root
        while current.getNextNode() is not prevNode.getData():
            current = current.getNextNode()
        newNode = node(d,current)
        prevNode.setNextNode(newNode)
    def print(self):
        current =self._root
        while current.getNextNode() is not None:
            print(current.getData())
            current = current.getNextNode()
        print(current.getData())





node1 = node(10,None)
node2 = node(1,2)
node3 = node (2,None)
print(node3)
L1 = linkedlist(node1)
L1.addFirst(36)
print(L1.addLast(7))
L1.print()
