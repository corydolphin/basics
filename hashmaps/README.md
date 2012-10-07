#hashmaps
Instructions for running practice problems:

```
python tests.py
```

##overview
[wikipedia]()

A hashmap is a key value store. It maps a key to a certain value. It's known as hashtables or Dictionaries in Python. 

Type in ```python``` to get to the python interpreter.

```
>>>a = {'a':5, 'b':10, 'c':15}
>>>a['a']
5
>>>a['b']
10
>>>a['c']
15

```

A hashmap uses a hashing function to determine the transformation between the keys (a, b, c) and the values (5, 10, 15). 

##common operations
###insertion
The time it takes to insert a new key value pair depends on how the hashmap is implementing collisions. It's impossible to have a perfect hashing function for every key value, so in the case that two keys map to the same hash value the hashmap needs to decide what to do.

Collisions can be handled by replacing the current value (what python does), or it could implement chaining (adding a linked list or an array as its value store). 

Insertion time for replacing the current value is O(1).

Insertion time for chaining is O(n) where n is proportional to the size of the linked list.

###deletion
Same as insertion. If the entire value can be deleted it's O(1), however if there is a list of values and only one is deleted it's O(n).
