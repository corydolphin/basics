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

###Mergesort

It's easiest to think of Merge Sort as consisting of two steps (at the highest level):

1. Break down an unsorted array into individual arrays of length 1 containing all the original array's elements.
2. Build back up the list, but now it's sorted.

The first step is O(n), which means that, in the worst case, the amount of time it takes step 1 to complete is
is some linear function of n. In other words there are n constant time operations required for it to complete.
In this case it is pretty clear why breaking down a list into it's individual elements takes n steps. You can simply
take each element in the given array, and place it in a new array, of length 1.  If an array has n elements, you need to do
the "move_to_array" operation n times.  

The second step is O(n*log(n)).  To see this observe the following tree:

1     3  9      4  10       13  7     15  \n
 \   /     \   /     \     /     \    /   \n
  1,3       4,9       10,13       7,15    \n
     \      /            \         /      \n
      1,3,4,9             7,10,13,15      \n
         \                    /           \n
           1,3,4,7,9,10,13,15             \n