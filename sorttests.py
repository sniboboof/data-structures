import simplesorting
import unittest
import random
import time

class InsertCase(unittest.TestCase):
    def testSelectionSort(self):
        answer = simplesorting.selectionsort([])
        assert answer == []
        answer = simplesorting.selectionsort([0])
        assert answer == [0]
        answer = simplesorting.selectionsort([0, 1])
        assert answer == [0, 1]
        answer = simplesorting.selectionsort([1, 0])
        assert answer == [0, 1]
        answer = simplesorting.selectionsort([-1, 1, 0])
        assert answer == [-1, 0, 1]
        answer = simplesorting.selectionsort([5, 4, 2, 4, 7, -25, None, 12])
        assert answer == [None, -25, 2, 4, 4, 5, 7, 12]
        sortinput = range(100)
        random.shuffle(sortinput)
        answer = simplesorting.selectionsort(sortinput)
        assert answer == range(100)

def timeselection(abignumber):
    myinput = range(abignumber)
    random.shuffle(myinput)
    start = time.time()
    simplesorting.selectionsort(myinput)
    stop = time.time()
    print "%d values in %s" % (abignumber, stop-start)

if __name__ == "__main__":
    timeselection(1000)
    timeselection(2000)
    timeselection(3000)
    timeselection(4000)
    timeselection(5000)
    timeselection(6000)

    unittest.main()