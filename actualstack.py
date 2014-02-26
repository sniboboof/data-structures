class jackstack:
    """stack that uses stacknodes"""
    def __init__(self):
        self.head = None
    
    def push(self, value):
        self.head = stacknode(value, self.head)
    
    def pop(self):
        result = self.head.value
        self.head = self.head.fwdNode
        return result


class stacknode:
    """simple node with a value and pointer to the next node"""
    def __init__(self, value, nextNode):
        self.value = value
        self.fwdNode = nextNode