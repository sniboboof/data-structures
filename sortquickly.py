import time
import treetests
import pdb
import sys

def speedysort(mylist):
    helpspeedysort(mylist, 0, len(mylist))
    return mylist

def helpspeedysort(mylist, start, end):
    if end - start <= 1:
        return mylist
    pivot = start
    pivotval = mylist[pivot]
    for i in xrange(start+1, end):
        if mylist[i] < pivotval:
            mylist[pivot] = mylist[i]
            mylist[i] = mylist[pivot+1]

            mylist[pivot+1] = pivotval
            pivot+=1
    helpspeedysort(mylist, start, pivot)
    helpspeedysort(mylist, pivot+1, end)

    return mylist

if __name__ == "__main__":
    #quicksort actually works like crap when
    #the list is already in order
    sys.setrecursionlimit(10100)
    a=range(10000)
    start = time.time()
    speedysort(a)
    stop = time.time()
    print "slowest: " + str(stop-start)
    a=[]
    #same perfect input as for binary search trees
    #kindof a similar algorithm too
    for i in treetests.perfectGenerator(0, 10000):
        a.append(i)
    start=time.time()
    speedysort(a)
    stop=time.time()
    print "fastest: " + str(stop-start)