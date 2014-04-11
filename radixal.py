def radixsort(mylist):
    if mylist == []:
        return []
    answerdict = {}
    for item in mylist:
        try:
            answerdict[item%10].append(item)
        except KeyError:
            answerdict[item%10] = [item, ]
    i = 1
    while len(answerdict.keys()) > 1:
        answerdict = radixhelper(answerdict, i)
        i += 1
    answerlist = answerdict.values()[0]
    return answerlist

def radixhelper(indict, digit):
    outdict={}
    for bucketlist in indict.values():
        for number in bucketlist:
            exactdigit = number
            for i in xrange(digit):
                exactdigit = exactdigit // 10
            exactdigit %= 10
            try:
                outdict[exactdigit].append(number)
            except KeyError:
                outdict[exactdigit] = [number, ]
    return outdict


def radixsortstring(mylist):
    if mylist == []:
        return []
    answerdict={'input':mylist}
    maxlength = 0
    for singlestring in mylist:
        maxlength = max(maxlength, len(singlestring))
    for i in xrange(maxlength):
        answerdict = radixstringhelper(answerdict, maxlength-(i+1))
    answerlist=[]
    for bucket in answerdict.values():
        answerlist.extend(bucket)
    return answerlist

def radixstringhelper(indict, index):
    shorties = indict.pop('shorties', [])
    outdict = {'shorties':[]}
    buckets = [shorties, ]
    for key in sorted(indict.keys()):
        buckets.append(indict[key])
    for bucketlist in buckets:
        for onestring in bucketlist:
            try:
                outdict[onestring[index]].append(onestring)
            except KeyError:
                outdict[onestring[index]] = [onestring, ]
            except IndexError:
                outdict['shorties'].append(onestring)
    worthlessstring = "alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu nu"
    return outdict
