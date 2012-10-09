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

    level 1: 1     3  9      4  10       13  7     15  
              \   /     \   /     \     /     \    /   
    level 2:   1,3       4,9       10,13       7,15    
                 \      /            \         /     
    level 3:      1,3,4,9             7,10,13,15      
                      \                    /           
    level 4:            1,3,4,7,9,10,13,15             

As you can see, at the top of the tree we have just completed step 1, we have separated an array into it's individual elements. Then are log(n) levels above this base level.  At each on of these levels we are merging and comparing the array from the level before.  We start off with the leftmost array on a level, and compare it to its neighbor.  We look at the lowest value in the left most array and compare it with the lowest value in the neighbor array.  Whichever value is lowest gets added to a new array.  We then do the same with the next lowest value in the left array, and so on, until the left array is empty.  At this point we know that everything in the right array is larger then everything in our new array, and we just add the remainder of the right array onto the new array.  The result is a merged and sorted version of the first two arrays on a level.  We then repeat this for the remaining arrays on a level.  

Now this combination of operations that occurs on each level to obtain the next level is O(n).  It's actual worst case runtime is less than n, but its some linear operation of n.  Obtaining the second level in the above tree takes at worst n steps, it takes n/4 steps to get the next level and finally n/2 steps to go from level 3 to level 4.