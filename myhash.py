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
            #return value
        except KeyError:
            print "invalid key"
            return None
    
    def set(self, key, value):
        bucketindex = self.hashin(key)
        self.buckets[bucketindex][key] = value