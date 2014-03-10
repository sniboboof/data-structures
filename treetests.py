import unittest
import bst
import cProfile
import time

class TestTree(unittest.TestCase):

    def testInsert(self):
        myTree = bst.treeNode()

        myTree.insert(5)
        myTree.insert(7)
        myTree.insert(3)
        myTree.insert(6)

        self.assertEqual(myTree.value, 5)
        self.assertEqual(myTree.right.value, 7)
        self.assertEqual(myTree.left.value, 3)
        self.assertEqual(myTree.right.left.value, 6)
        self.assertEqual(myTree.right.left.right.value, None)

    def testContains(self):
        myTree = bst.treeNode()
        for item in (5, 3, 7, 1, 2, 8, 4):
            myTree.insert(item)

        self.assertEqual(myTree.contains(5), True)
        self.assertEqual(myTree.contains(2), True)
        self.assertEqual(myTree.contains(743), False)

    def testSize(self):
        myTree = bst.treeNode()
        self.assertEqual(myTree.size(), 0)

        myTree.insert(5)
        self.assertEqual(myTree.size(), 1)

        myTree.insert(3)
        self.assertEqual(myTree.size(), 2)

        myTree.insert(7)
        self.assertEqual(myTree.size(), 3)

        myTree.insert(4)
        self.assertEqual(myTree.size(), 4)

    def testDepth(self):
        myTree = bst.treeNode()
        self.assertEqual(myTree.depth(), 0)

        myTree.insert(5)
        self.assertEqual(myTree.depth(), 1)

        myTree.insert(3)
        self.assertEqual(myTree.depth(), 2)

        myTree.insert(7)
        self.assertEqual(myTree.depth(), 2)

        myTree.insert(4)
        self.assertEqual(myTree.depth(), 3)

    def testBalance(self):
        myTree = bst.treeNode()
        self.assertEqual(myTree.balance(), 0)

        myTree.insert(5)
        self.assertEqual(myTree.balance(), 0)

        myTree.insert(3)
        self.assertEqual(myTree.balance(), 1)

        myTree.insert(7)
        self.assertEqual(myTree.balance(), 0)

        myTree.insert(6)
        self.assertEqual(myTree.balance(), -1)

def perfectRange(start, end):
    midi = (end-start)/2
    yield midi+start
    yield perfectRange(start, start+midi)
    yield perfectRange(start+midi+1, end)

if __name__ == "__main__":
    print "testing best and worst case speeds for values in range(2^9 - 1)"
    
    myTree = bst.treeNode()
    for good in perfectRange(0, 511):
        myTree.insert(good)
    
    start = time.time()
    myTree.contains(510)
    stop = time.time()
    
    print str(stop-start)
    
    myTree = bst.treeNode()
    for bad in xrange(511):
        myTree.insert(bad)
    
    start = time.time()
    myTree.contains(510)
    stop = time.time()
    
    print str(stop-start)
    unittest.main()