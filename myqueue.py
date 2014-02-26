class qNode:
    def __init__(self, value, node_in_front):
        self.nextnode = node_in_front
        self.item = value
        self.prevnode = None

class ezQueue:
    def __init__(self):
        self.numnodes = 0
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        newNode = qNode(value, self.head)
        if self.head:
            self.head.prevnode = newNode
        else:
            self.tail = newNode
        self.head = newNode
        
        self.numnodes += 1
    
    def dequeue(self):
        try:
            oldNode = self.tail
            self.tail = oldNode.prevnode
            if self.tail:
                self.tail.nextnode = None
            
            self.numnodes -= 1
            if self.numnodes == 0:
                self.head = None
            return oldNode.item
        except AttributeError:
            print "This queue is empty"
            return None
    
    def size(self):
        return self.numnodes