import insertsort
import unittest
import random
import time

class InsertCase(unittest.TestCase):
    def testSort(self):
        answer = insertsort.insertsort([])
        assert answer == []
        answer = insertsort.insertsort([0])
        assert answer == [0]
        answer = insertsort.insertsort([0, 1])
        assert answer == [0, 1]
        answer = insertsort.insertsort([1, 0])
        assert answer == [0, 1]
        answer = insertsort.insertsort([-1, 1, 0])
        assert answer == [-1, 0, 1]
        answer = insertsort.insertsort([5, 4, 2, 4, 7, -25, None, 12])
        assert answer == [None, -25, 2, 4, 4, 5, 7, 12]
        sortinput = range(100)
        random.shuffle(sortinput)
        answer = insertsort.insertsort(sortinput)
        assert answer == range(100)

def timeinsert(abignumber):
    myinput = range(abignumber)
    random.shuffle(myinput)
    start = time.time()
    insertsort.insertsort(myinput)
    stop = time.time()
    print "%d values in %s" % (abignumber, stop-start)

if __name__ == "__main__":
    timeinsert(1000)
    timeinsert(2000)
    timeinsert(3000)
    timeinsert(4000)
    timeinsert(5000)
    timeinsert(6000)

    unittest.main()