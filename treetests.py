import unittest
import bst
import cProfile
import time
import random

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

    def testInOrder(self):
        myTree = bst.treeNode()
        for i in [59, 73, 75, 90, 63, 5, 9, 66, 1, 74, 18, 68, 27,
                  35, 60, 6, 23, 34, 98, 56, 42, 31, 28, 47, 46, 8,
                  45, 2, 13, 97, 0, 96, 85, 62, 79, 93, 16, 17, 30,
                  94, 37, 22, 3, 71, 44, 48, 76, 99, 39, 19, 20, 83,
                  41, 21, 81, 51, 29, 70, 88, 14, 24, 77, 84, 55,
                  57, 32, 95, 4, 80, 86, 78, 58, 7, 11, 43, 52, 53,
                  67, 92, 69, 61, 65, 64, 49, 25, 36, 50, 89, 82,
                  15, 38, 10, 40, 26, 91, 54, 33, 12, 72, 87
        ]:
            myTree.insert(i)
        index = 0
        for a in myTree.in_order():
            self.assertEqual(a, index)
            index+=1

    def testPreOrder(self):
        myTree = bst.treeNode()
        for i in [59, 73, 75, 90, 63, 5, 9, 66, 1, 74, 18, 68, 27,
                  35, 60, 6, 23, 34, 98, 56, 42, 31, 28, 47, 46, 8,
                  45, 2, 13, 97, 0, 96, 85, 62, 79, 93, 16, 17, 30,
                  94, 37, 22, 3, 71, 44, 48, 76, 99, 39, 19, 20, 83,
                  41, 21, 81, 51, 29, 70, 88, 14, 24, 77, 84, 55,
                  57, 32, 95, 4, 80, 86, 78, 58, 7, 11, 43, 52, 53,
                  67, 92, 69, 61, 65, 64, 49, 25, 36, 50, 89, 82,
                  15, 38, 10, 40, 26, 91, 54, 33, 12, 72, 87
        ]:
            myTree.insert(i)
        answer = [59, 5, 1, 0, 2, 3, 4, 9, 6, 8, 7, 18, 13, 11, 10,
                  12, 16, 14, 15, 17, 27, 23, 22, 19, 20, 21, 24,
                  25, 26, 35, 34, 31, 28, 30, 29, 32, 33, 56, 42,
                  37, 36, 39, 38, 41, 40, 47, 46, 45, 44, 43, 48,
                  51, 49, 50, 55, 52, 53, 54, 57, 58, 73, 63, 60,
                  62, 61, 66, 65, 64, 68, 67, 71, 70, 69, 72, 75,
                  74, 90, 85, 79, 76, 77, 78, 83, 81, 80, 82, 84,
                  88, 86, 87, 89, 98, 97, 96, 93, 92, 91, 94, 95, 99]
        i = 0
        for a in myTree.pre_order():
            self.assertEqual(a, answer[i])
            i+=1

    def testPostOrder(self):
        myTree = bst.treeNode()
        for i in [59, 73, 75, 90, 63, 5, 9, 66, 1, 74, 18, 68, 27,
                  35, 60, 6, 23, 34, 98, 56, 42, 31, 28, 47, 46, 8,
                  45, 2, 13, 97, 0, 96, 85, 62, 79, 93, 16, 17, 30,
                  94, 37, 22, 3, 71, 44, 48, 76, 99, 39, 19, 20, 83,
                  41, 21, 81, 51, 29, 70, 88, 14, 24, 77, 84, 55,
                  57, 32, 95, 4, 80, 86, 78, 58, 7, 11, 43, 52, 53,
                  67, 92, 69, 61, 65, 64, 49, 25, 36, 50, 89, 82,
                  15, 38, 10, 40, 26, 91, 54, 33, 12, 72, 87
        ]:
            myTree.insert(i)
        answer = [0, 4, 3, 2, 1, 7, 8, 6, 10, 12, 11, 15, 14, 17,
                  16, 13, 21, 20, 19, 22, 26, 25, 24, 23, 29, 30,
                  28, 33, 32, 31, 34, 36, 38, 40, 41, 39, 37, 43,
                  44, 45, 46, 50, 49, 54, 53, 52, 55, 51, 48, 47,
                  42, 58, 57, 56, 35, 27, 18, 9, 5, 61, 62, 60,
                  64, 65, 67, 69, 70, 72, 71, 68, 66, 63, 74, 78,
                  77, 76, 80, 82, 81, 84, 83, 79, 87, 86, 89, 88,
                  85, 91, 92, 95, 94, 93, 96, 97, 99, 98, 90, 75,
                  73, 59]
        i = 0
        for a in myTree.post_order():
            self.assertEqual(a, answer[i])
            i+=1

    def testBreadthFirst(self):
        myTree = bst.treeNode()
        for i in [59, 73, 75, 90, 63, 5, 9, 66, 1, 74, 18, 68, 27,
                  35, 60, 6, 23, 34, 98, 56, 42, 31, 28, 47, 46, 8,
                  45, 2, 13, 97, 0, 96, 85, 62, 79, 93, 16, 17, 30,
                  94, 37, 22, 3, 71, 44, 48, 76, 99, 39, 19, 20, 83,
                  41, 21, 81, 51, 29, 70, 88, 14, 24, 77, 84, 55,
                  57, 32, 95, 4, 80, 86, 78, 58, 7, 11, 43, 52, 53,
                  67, 92, 69, 61, 65, 64, 49, 25, 36, 50, 89, 82,
                  15, 38, 10, 40, 26, 91, 54, 33, 12, 72, 87
        ]:
            myTree.insert(i)
        answer = [59, 5, 73, 1, 9, 63, 75, 0, 2, 6, 18, 60, 66, 74,
                  90, 3, 8, 13, 27, 62, 65, 68, 85, 98, 4, 7, 11,
                  16, 23, 35, 61, 64, 67, 71, 79, 88, 97, 99, 10,
                  12, 14, 17, 22, 24, 34, 56, 70, 72, 76, 83, 86,
                  89, 96, 15, 19, 25, 31, 42, 57, 69, 77, 81, 84,
                  87, 93, 20, 26, 28, 32, 37, 47, 58, 78, 80, 82,
                  92, 94, 21, 30, 33, 36, 39, 46, 48, 91, 95, 29,
                  38, 41, 45, 51, 40, 44, 49, 55, 43, 50, 52, 53,
                  54]
        gen = myTree.breadth_first()
        for i in range(100):
            print answer[i]
            self.assertEqual(gen.next(), answer[i])
        self.assertRaises(StopIteration, gen.next())

def perfectRange(start, end):
    answer = []

    perfectCenter(start, end, answer)

    return answer

def perfectCenter(start, end, answer):
    midi = (end-start)/2
    answer.append(midi+start)

    if midi > 0:
        perfectCenter(start, start+midi, answer)
    if start+midi != end-1:
        perfectCenter(start+midi+1, end, answer)

def perfectGenerator(start, end):
    midi = (end-start)/2
    yield midi+start

    if midi > 0:
        for i in perfectGenerator(start, start+midi):
            yield i
    if start+midi != end-1:
        for i in perfectGenerator(start+midi+1, end):
            yield i

if __name__ == "__main__":
    print "testing best and worst case speeds for values in range(2^9 - 1)"

    myTree = bst.treeNode()
    for good in perfectRange(0, 511):
        myTree.insert(good)

    start = time.time()
    myTree.contains(510)
    stop = time.time()

    print str(stop-start)
    # myfile = open("good.dot", "w")
    # myfile.write(myTree.get_dot())
    # myfile.close()

    myTree = bst.treeNode()
    for bad in xrange(511):
        myTree.insert(bad)

    start = time.time()
    myTree.contains(510)
    stop = time.time()

    print str(stop-start)
    # myfile = open("bad.dot", "w")
    # myfile.write(myTree.get_dot())
    # myfile.close()

    random.seed()
    myrange = range(511)
    random.shuffle(myrange)
    myTree = bst.treeNode()
    for i in myrange:
        myTree.insert(i)
    # myfile = open("other.dot", "w")
    # myfile.write(myTree.get_dot())
    # myfile.close()

    unittest.main()