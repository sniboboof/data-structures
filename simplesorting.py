def selectionsort(mylist):
    for i in xrange(len(mylist)):
        ansindex = i
        for j in xrange(i+1, len(mylist)):
            if mylist[ansindex] > mylist[j]:
                ansindex=j
        mylist[i], mylist[ansindex] = mylist[ansindex], mylist[i]
    return mylist

def insertionsort(mylist):
    for i in xrange(1, len(mylist)):
        j=i-1
        val = mylist[i]
        while mylist[j] > val and j>=0:
            mylist[j+1]=mylist[j]
            mylist[j]=val
            j-=1
    return mylist