#arrays
Instructions for running practice problems:

```
python tests.py
```

##overview
[wikipedia](http://en.wikipedia.org/wiki/Array_data_structure)

An array contains a list of values, each with a particular index. The index can be mapped to an address in memory which makes iteration through an array much faster than that of a linked list. 

##common operations
###sorting
There are multiple ways to sort an array, but the most common are

* [quicksort](http://en.wikipedia.org/wiki/Quicksort) Best: O(n*log(n)), Worst: O(n^2)
* [mergesort](http://en.wikipedia.org/wiki/Mergesort) O(n*log(n))

Quicksort has the same average speed as mergesort, but uses much less space.
