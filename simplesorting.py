def selectionsort(mylist):
    for i in xrange(len(mylist)):
        ansindex = i
        for j in xrange(i+1, len(mylist)):
            if mylist[ansindex] > mylist[j]:
                ansindex=j
        mylist[i], mylist[ansindex] = mylist[ansindex], mylist[i]
    return mylist