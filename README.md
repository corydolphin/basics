#basics

This is a series of ongoing slac notes & exercises.

##week 1
* big O notation
* linked lists
* arrays
* hash maps  

###Big O notation/runtime complexity
[wikipedia](http://en.wikipedia.org/wiki/Big_o_notation)

[sicp chapter 1.2](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2)

The basic question that big O notation is trying to answer is: **how many steps does it take to compute a solution**?

It's a quick calculation of the **speed of an algorithm**. Let's say we have the following program to calculate factorials:

```python
def factorial(n):
	print "factorial called with", n
	if (n == 1):
		return 1
	return n * (factorial(n-1))
```

Obviously the speed to calculate the factorial of 6 is a lot faster than the speed to calculate, say, 10391352. So we calculate big O with respect to *n*, in this case the input number. 

So what's the runtime? Let's say we run
```
factorial(6)
```

Here are the steps that it would require:
<pre>
factorial(6)
	factorial(5)
		factorial(4)
			factorial(3)
				factorial(2)
					factorial(1)
</pre>

And as you increase the number *n*, the number of calls it would make to factorial grow in a linear proportion to *n*. It's O(n).

You can choose *n* to be whatever you like but by convention it's usually picked as whatever number is easiest to calculate. For example, when dealing with linked lists, *n* will probably be the length of the list.

There are a few common speeds of algorithms:

* Constant: O(1)
* Linear: O(n)
* Quadratic: O(n^2)
* Logrithmic: O(log(n))

Obviously you want to strive for the lowest runtime complexity. However in most scenarios you will have to make a tradeoff between memory and speed.
  
##week 0
* set up a [github](https://github.com/) account
* set up your computer with either linux or mac
* get a text editor. suggested editors: sublime, textmate

###linux install

* get [ubuntu](http://www.ubuntu.com/download/desktop). a 10-15 gig partition is sufficient
* setup python
```
easy_install pip
sudo pip install virtualenv
```

###mac install
* get [xcode](https://developer.apple.com/xcode/)
* install [brew](http://mxcl.github.com/homebrew/) 
```ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)"```
* setup python
```
easy_install pip
sudo pip install virtualenv
```
