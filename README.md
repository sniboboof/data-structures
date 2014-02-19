File linked_list.py
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