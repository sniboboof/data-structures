import myqueue
import unittest

class testQueue(unittest.TestCase):
    def setUp(self):
        self.sample_queue = None
    
    def test_enqueue(self):
        self.sample_queue = myqueue.ezQueue()
        for i in range(3):
            self.sample_queue.enqueue(i)
            self.assertEqual(i, self.sample_queue.head.item)
            self.assertEqual(0, self.sample_queue.tail.item)
        
        self.sample_queue.enqueue(None)
        self.assertEqual(None, self.sample_queue.head.item)
        
        self.sample_queue.enqueue("butwhy")
        self.assertEqual("butwhy", self.sample_queue.head.item)
    
    def test_dequeue(self):
        #assume enqueue passed
        self.sample_queue = myqueue.ezQueue()
        for i in range(3):
            self.sample_queue.enqueue(i)
        
        for i in range(3):
            self.assertEqual(i, self.sample_queue.tail.item)
            self.assertEqual(i, self.sample_queue.dequeue())
        self.assertEqual(None, self.sample_queue.head)
        self.assertEqual(None, self.sample_queue.tail)
        
        self.assertEqual(None, self.sample_queue.dequeue())
    
    def test_size(self):
        self.sample_queue = myqueue.ezQueue()
        self.assertEqual(0, self.sample_queue.size())
        
        for i in range(5):
            self.sample_queue.enqueue(i)
            self.assertEqual(i+1, self.sample_queue.size())
        
        for i in range(4, -1, -1):
            self.sample_queue.dequeue()
            self.assertEqual(i, self.sample_queue.size())
        self.sample_queue.dequeue()
        self.assertEqual(0, self.sample_queue.size())

if __name__ == "__main__":
    unittest.main()