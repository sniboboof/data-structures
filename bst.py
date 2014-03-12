import random

class treeNode():
    """node of a binary search tree. functions as root or branch"""
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

    def insert(self, comparable):
        #None is technically comparable but no.
        if comparable is None:
            raise TypeError

        if self.value is None:
            self.value = comparable
            self.left = treeNode()
            self.right = treeNode()
        elif comparable < self.value:
            self.left.insert(comparable)
        elif comparable > self.value:
            self.right.insert(comparable)
        else: #trying to insert two of the same value
            return

    def contains(self, comparable):
        if self.value is None:
            return False
        elif comparable < self.value:
            return self.left.contains(comparable)
        elif comparable > self.value:
            return self.right.contains(comparable)
        else: #comparable == self.value:
            return True

    def size(self):
        if self.value is None:
            return 0
        else:
            return self.left.size()+self.right.size()+1

    def depth(self):
        if self.value is None:
            return 0
        else:
            return max(self.left.depth(), self.right.depth()) + 1

    def balance(self):
        if self.value is None:
            return 0
        else:
            return self.left.depth() - self.right.depth()

    def in_order(self):
        if self.value is None:
            return
        for i in self.left.in_order():
            yield i
        yield self.value
        for i in self.right.in_order():
            yield i

    def pre_order(self):
        if self.value is None:
            return
        yield self.value
        for i in self.left.pre_order():
            yield i
        for i in self.right.pre_order():
            yield i

    def post_order(self):
        if self.value is None:
            return
        for i in self.left.post_order():
            yield i
        for i in self.right.post_order():
            yield i
        yield self.value

    def breadth_first(self):
        for i in self._breadth_first():
            yield i[1].value

    #helper function for breadth first, needs to return height and node
    def _breadth_first(self,):
        if self.value is None:
            return
        lGen = self.left._breadth_first()
        rGen = self.right._breadth_first()
        try:
            lheight, lindex = lGen.next()
        except StopIteration:
            return
        try:
            rheight, rindex = rGen.next()
        except StopIteration:
            return
        for height in range(1, self.depth()):
            while lindex.value is not None or rindex.value is not None:
                while height == lheight:
                    yield lheight+1, lindex
                    try:
                        lheight, lindex = lGen.next()
                    except StopIteration:
                        return

                while height == rheight:
                    yield rheight+1, rindex
                    try:
                        rheight, rindex = rGen.next()
                    except StopIteration:
                        return

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.value is None else (
            "\t%s;\n%s\n" % (
                self.value,
                "\n".join(self._get_dot())
            )
        ))

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left.value is not None:
            yield "\t%s -> %s;" % (self.value, self.left.value)
            for i in self.left._get_dot():
                yield i
        elif self.right.value is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)
        if self.right.value is not None:
            yield "\t%s -> %s;" % (self.value, self.right.value)
            for i in self.right._get_dot():
                yield i
        elif self.left.value is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)
