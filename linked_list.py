import unittest

class mynode:
    """node for linked list"""
    
    def __init__(self, init, tail):
        self.value = init
        self.linknext = tail
    


class mystack:
    """singly linked list for python class"""
    
    def __init__(self):
        self.head = None
        self.len = 0
    
    def insert(self, val):
        newNode = mynode(val, self.head)
        self.head = newNode
        self.len += 1
    
    def pop(self):
        if not self.head:
            return None
        poppednode = self.head
        self.head = poppednode.linknext
        self.len = self.len - 1
        return poppednode.value
    
    def size(self):
        return self.len
    
    def search(self, searchterm):
        currentNode = self.head
        while currentNode:
            if currentNode.value == searchterm:
                return currentNode
            currentNode = currentNode.linknext
        return None
    
    def remove(self, deletingnode):
        currentNode = self.head
        if not currentNode:
            return
        if currentNode == deletingnode:
            self.head = deletingnode.next
            self.len = self.len - 1
        while True:
            if not currentNode:
                return
            if currentNode.linknext == deletingnode:
                break
            currentNode = currentNode.linknext
        currentNode.linknext = deletingnode.linknext
        self.len= self.len - 1
    
    def __str__(self):
        mess = '('
        currentNode = self.head
        if not currentNode:
            return None
        while True:
            if type(currentNode.value) == type(''):
                mess +="'"
            mess += str(currentNode.value)
            if type(currentNode.value) == type(''):
                mess +="'"
            currentNode = currentNode.linknext
            if not currentNode:
                break
            mess += ', '
        mess += ')'
        return mess

class TestLinkedList(unittest.TestCase):
    
    def test_mylist(self):
        alist=mystack()
        self.assertEqual(alist.head, None)
    
    def test_insert_pop(self):
        alist = mystack()
        for i in range(10):
            alist.insert(i)
        
        for i in range(9, -1):
            self.assertEqual(i, alist.pop())
    
    def test_len(self):
        alist = mystack()
        self.assertEqual(alist.size(), 0)
        alist.insert(0)
        self.assertEqual(alist.size(), 1)
        alist.insert(0)
        self.assertEqual(alist.size(), 2)
        alist.pop()
        self.assertEqual(alist.size(), 1)
    
    def test_remove(self):
        alist = mystack()
        for i in range(3):
            alist.insert(i)
        alist.remove(alist.search(1))
        self.assertEqual(str(alist), """(2, 0)""")
    
    def test_search(self):
        alist = mystack()
        for i in range(17):
            alist.insert(i)
        foundnode = alist.search(4)
        self.assertEqual(foundnode.value, 4)
    
    def test_print(self):
        alist = mystack()
        for i in range(10):
            alist.insert(i)
        alist.insert("Wyoming")
        self.assertEqual(str(alist), """('Wyoming', 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)""")

if __name__ == '__main__':
    unittest.main()