import actualstack

class ezHash(object):
    """docstring for ezHash"""
    def __init__(self, max_size):
        self.bucketnum = max_size
        self.buckets = []
        for i in range(max_size):
            self.buckets.append({})
    
    def hashin(self, word):
        total = 0
        for c in word:
            total += ord(c)
        return total % self.bucketnum
    
    def get(self, key):
        bucketindex = self.hashin(key)
        try:
            return self.buckets[bucketindex][key]
        except KeyError:
            print "invalid key"
            return None
    
    def set(self, key, value):
        bucketindex = self.hashin(key)
        self.buckets[bucketindex][key] = value

class linkHash(object):
    """docstring for linkHash"""
    def __init__(self, max_size):
        self.bucketnum = max_size
        self.buckets = actualstack.jackstack()
        for i in range(self.bucketnum):
            self.buckets.push({})
    
    def hashin(self, word):
        total = 0
        for c in word:
            total += ord(c)
        return total % self.bucketnum
    
    def get(self, key):
        bucketindex = self.hashin(key)
        currentbucket = self.buckets.head
        for i in range(bucketindex-1):
            currentbucket = currentbucket.fwdNode
        try:
            return currentbucket.value[key]
        except KeyError:
            print "invalid key"
            return None
    
    def set(self, key, value):
        bucketindex = self.hashin(key)
        currentbucket = self.buckets.head
        for i in range(bucketindex-1):
            currentbucket = currentbucket.fwdNode
        currentbucket.value[key] = value