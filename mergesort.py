import time
import random

def mergesort(mylist):
    mergehelper(mylist, 0, len(mylist))
    return mylist

def mergehelper(mylist, start, end):
    if end-start <= 1:
        return mylist

    halfway = start + (end-start)/2
    mergehelper(mylist, start, halfway)
    mergehelper(mylist, halfway, end)

    while start < halfway and halfway < end:
        if mylist[start] <= mylist[halfway]:
            start+=1
        else:
            insertpartial(mylist, mylist[halfway], start, halfway)
            start+=1
            halfway+=1

    return mylist

def insertpartial(mylist, value, index, end):
    #similar to list.insert() but works over only part of a list
    #list.insert is O(n) where n is the length of the WHOLE list
    #this only inserts over part of the list, so it's O(n) over
    #this part of the list, averaging out to O(log n) for the function
    #i think
    tempval=mylist[index]
    mylist[index] = value
    for i in range(index+1, end+1):
        value = tempval
        tempval = mylist[i]
        mylist[i] = value

if __name__ == "__main__":
    a=range(10000)
    #worst part of the algorithm is insertpartial
    #so if you never have to call that (it's in order)
    #it goes faster
    start = time.time()
    mergesort(a)
    stop = time.time()
    print "fastest: " + str(stop-start)
    #and it will be the worst when it insertpartials every time
    #so reverse order
    a.reverse()
    start=time.time()
    mergesort(a)
    stop=time.time()
    print "slowest: " + str(stop-start)