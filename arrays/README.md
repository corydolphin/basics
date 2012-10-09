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

Now this combination of operations that occurs on each level to obtain the next level is O(n) (for each level).  You might have noticed that it's actual worst case runtime is less than n.  Obtaining the second level in the above tree takes at worst n steps, it takes n/4 steps to get the next level and finally n/2 steps to go from level 3 to level 4.  However as long as runtime is dependent on some linear operation on n, like / + - or x, the big O is just n.

So it the big O of going from one level to the next is n.  Now to find the big O of the entire merge operation we can just multiply n by the number of times we have to move up a level, which is log(n) (log in big 0 is always log base 2). This gives us a final big O of n*log(n) for the merge operation (step 2 of the two steps I laid out above).

We now know that step 1 of merge sort is O(n) and step 2 is O(n*log(n)), so what is the big O for the entire merge sort? Well, technically its O(n+n*log(n)), however, we can just ignore the "n +" part here.  To see this just rewrite n + n*log(n) as n*(1+log(n)), and as 1+log(n) is just a linear operation on log(n), we can get rid of the 1, leaving just n*log(n).  

Merge sort, with it's n*log(n) runtime, is the fastest sort around, way faster then sorts like bubble sort or insertion sort which both take n^2 time.  Quicksort, another commonly used sort algorithm also has a worst case of n^2, however it's average case runtime is n*log(n) like merge sort, and it takes less space.  Read about quicksort using the link above for now.  We'll throw an explanation up here on the github in a bit.   