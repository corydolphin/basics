#linked lists
Instructions for running practice problems:

```
pip install requirements.txt
python linked_list.py
```

##overview
[wikipedia](http://en.wikipedia.org/wiki/Linked_lists)

A linked list is a data structure that consists of a chain of nodes. Each node has the data that is contained within the node and a reference to the next node. 

This way of referencing next/previous nodes is the only way to get from one node to the next.

###singly linked lists
<pre>
[node 1] -> [node 2] -> [node 3]
  ^            ^
  head node    tail
</pre>

Each node has a reference to the next node. The final node has a null reference which designates the end of the linked list.

###doubly linked lists
<pre>
[node 1] <=> [node 2] <=> [node 3]
</pre>

Each node has a link to the next node and a link to the previous node.

###circular linked lists
<pre>
[node 1] -> [node 2] -> [node 3] -> [node 4]
	           ^                        |
	           |-------------------------
</pre>

A singly linked list with a cycle.

##common operations
###insertion
<pre>
[node 1] -> [node 2] -> [node 3]

to

[node 1] -> [node 2] -> [node 2.5] -> [node 3]
</pre>

Takes O(n) (linear time) to insert a new node anywhere but the beginning of the list. You have to walk through the list until you find the place where you want to insert the new node. Once you find it, you have to set the previous node's link to point at the new node. The new node then points at the next node.

Takes O(1) (constant time) to insert a new node at the start of the list. This just involves creating a new node and setting it's next link to the current head of the list.

###deletion
<pre>
[node 1] -> [node 2] -> [node 3]

to

[node 1] -> [node 3]
</pre>

Similar to insertion:

* Takes O(n) to delete a node anywhere not at the start of the list.
* Takes O(1) to delete a node at the start of the list.

###finding
Takes O(n) to find a node with a particular value. You have to walk through the list until you find the right node.
