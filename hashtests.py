import myhash
import unittest

class testHash(unittest.TestCase):
    """docstring for testHash"""
    def setUp(self):
        self.samplehash = None
    
    def testHash(self):
        self.samplehash = myhash.ezHash(1024)
        self.assertEqual(self.samplehash.hashin("a"), ord('a'))
        
        self.samplehash = myhash.ezHash(4)
        self.assertEqual(self.samplehash.hashin("a"), ord('a')%4)
        self.assertEqual(self.samplehash.hashin(""), 0)
        
        self.samplehash = myhash.ezHash(20)
        self.assertEqual(self.samplehash.hashin("ab"), (ord('a')+ord('b')) % 20)
        mess = """abcdefghijklmnopqrstuvwxyz The quick brown fox jumps over the lazy dog lorem ipsum arghwarblesjfhurhp./.,jxcviwpiou\n\r ''' "ffdhhowuo\\sdfo " ' ""' """
        total = 0
        for c in mess:
            total += ord(c)
        self.assertEqual(self.samplehash.hashin(mess), total%20)
    
    def testSetGetSingle(self):
        self.samplehash = myhash.ezHash(20)
        
        self.assertEqual(self.samplehash.get("potato"), None)
        
        samplewords = ("aaa", "aab", "aac", "aad")
        for i in range(len(samplewords)):
            self.samplehash.set(samplewords[i], i)
        
        for i in range(len(samplewords)):
            self.assertEqual(self.samplehash.get(samplewords[i]), i)
            self.assertRaises(KeyError, lambda: self.samplehash.buckets[(i+1) % 20][samplewords[i]])
    
    def testSetGetMultiple(self):
        self.samplehash = myhash.ezHash(1024)
        wordfile = open("/usr/share/dict/words", "r")
        samplewords = wordfile.read().split()
        wordfile.close()
        
        for i in range(len(samplewords)):
            self.samplehash.set(samplewords[i], i)
        
        for i in range(len(samplewords)):
            self.assertEqual(self.samplehash.get(samplewords[i]), i)

if __name__ == "__main__":
    unittest.main()