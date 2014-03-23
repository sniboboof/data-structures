import simplesorting
import mergesort
import sortquickly
import unittest
import random
import time
import radixal

def sorttestframework(sortfunction):
    answer = sortfunction([])
    assert answer == []
    answer = sortfunction([0])
    assert answer == [0]
    answer = sortfunction([0, 1])
    assert answer == [0, 1]
    answer = sortfunction([1, 0])
    assert answer == [0, 1]
    answer = sortfunction([-1, 1, 0])
    assert answer == [-1, 0, 1]
    answer = sortfunction([5, 4, 2, 4, 7, -25, None, 12])
    assert answer == [None, -25, 2, 4, 4, 5, 7, 12]
    sortinput = range(100)
    random.shuffle(sortinput)
    answer = sortfunction(sortinput)
    assert answer == range(100)

class sortCase(unittest.TestCase):

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

    def testInsertionSort(self):
        answer = simplesorting.insertionsort([])
        assert answer == []
        answer = simplesorting.insertionsort([0])
        assert answer == [0]
        answer = simplesorting.insertionsort([0, 1])
        assert answer == [0, 1]
        answer = simplesorting.insertionsort([1, 0])
        assert answer == [0, 1]
        answer = simplesorting.insertionsort([-1, 1, 0])
        assert answer == [-1, 0, 1]
        answer = simplesorting.insertionsort([5, 4, 2, 4, 7, -25, None, 12])
        assert answer == [None, -25, 2, 4, 4, 5, 7, 12]
        sortinput = range(100)
        random.shuffle(sortinput)
        answer = simplesorting.insertionsort(sortinput)
        assert answer == range(100)

    def testMerge(self):
        sorttestframework(mergesort.mergesort)

    def testSpeedy(self):
        sorttestframework(sortquickly.speedysort)

    def testRadix(self):
        #radix sort doesn't work with negative numbers
        answer = radixal.radixsort([])
        assert answer == []
        answer = radixal.radixsort([0])
        assert answer == [0]
        answer = radixal.radixsort([0, 1])
        assert answer == [0, 1]
        answer = radixal.radixsort([1, 0])
        assert answer == [0, 1]
        answer = radixal.radixsort([1, 1, 0])
        assert answer == [0, 1, 1]
        answer = radixal.radixsort([5, 4, 2, 4, 7, 25, 12])
        assert answer == [2, 4, 4, 5, 7, 12, 25]
        sortinput = range(1000000)
        random.shuffle(sortinput)
        answer = radixal.radixsort(sortinput)
        assert answer == range(1000000)

    def testRadixString(self):
        answer = radixal.radixsortstring([])
        assert answer == []
        answer = radixal.radixsortstring(["a"])
        assert answer == ["a"]
        answer = radixal.radixsortstring(["a", "b"])
        assert answer == ["a", "b"]
        answer = radixal.radixsortstring(["b", "a"])
        assert answer == ["a", "b"]
        answer = radixal.radixsortstring(["a", "bc"])
        assert answer == ["a", "bc"]
        answer = radixal.radixsortstring(["bc", "a"])
        assert answer == ["a", "bc"]
        answer = radixal.radixsortstring(["ab", "a", "bc"])
        assert answer == ["a", "ab", "bc"]
        answer = radixal.radixsortstring(["cae", "cad", "alphabet", "cad", "jack markley", "zylophone"])
        assert answer == ["alphabet", "cad", "cad", "cae", "jack markley", "zylophone"]

def timeselection(abignumber):
    myinput = range(abignumber)
    random.shuffle(myinput)
    start = time.time()
    simplesorting.selectionsort(myinput)
    stop = time.time()
    print "%d values in %s" % (abignumber, stop-start)

def timeinsertion(abignumber):
    myinput = range(abignumber)
    random.shuffle(myinput)
    start = time.time()
    simplesorting.insertionsort(myinput)
    stop = time.time()
    print "%d values in %s" % (abignumber, stop-start)

if __name__ == "__main__":
    # timeselection(1000)
    # timeselection(2000)
    # timeselection(3000)
    # timeselection(4000)
    # timeselection(5000)
    # timeselection(6000)
    # timeinsertion(1000)
    # timeinsertion(2000)
    # timeinsertion(3000)
    # timeinsertion(4000)
    # timeinsertion(5000)
    # timeinsertion(6000)

    unittest.main()