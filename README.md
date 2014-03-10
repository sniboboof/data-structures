LINKED LIST
contains two classes: mystack and mynode
mynode is a simple node with a value and a link to another node, when initialized you need to pass both a value and the node that will follow it in the list to the constructor
mystack is a container for the list of mynodes. it has a head and len attribute that track the top node in the list and the current length of the list, respectively.

mystack contains several members that traverse and change the list:
insert(value) creates a node containing the value and sets it as the new head of the list, then increments the list's length
remove(node) will find the node and remove it from the list without breaking the list
search(value) will find the first node with the value in the list and return that node
pop() removes the head from the list and returns its value
size() returns the length of the list

the list works with the str() built-in function and returns a string similar to a tuple containing the values in the list.

STACK
<INSERT STACK DESCRIPTION>

QUEUE
<INSERT QUEUE DESCRIPTION>

HASH
<INSERT HASH DESCRIPTION>

CALENDAR
<INSERT CALENDAR DESCRIPTION>

BINARY SEARCH TREE
treeNode object handles both a full tree and individual nodes
insert(value) inserts a comparable value into the tree. inserting None returns an error

contains(value) checks the tree for a comparable value.

size() returns the number of nodes in the tree.

depth() returns the depth of the deepest node in the tree

balance() returns a comparison of the depths of each side of the tree, giving a rough estimate of the tree's efficiency

note that the tree produces empty nodes at the ends of each branch in case they need to be inserted into later (leaves). this is somewhat memory inefficient and may be changed later.
