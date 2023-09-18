# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

*Yes, but pop in dict will return its value.*

1. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

*List: use dynamic array. Ordered.*
*Dict: use hash table. Not ordered. Stores key-value pairs. Key is unique.*

1. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

*Yes*

1. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

*Pros: Flexible and make code shorter*
*Cons: Slow and may increase risks of errors*

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

*Yes. E.g. sending requests just requires the name of HTTP methods (GET, PUT...)*

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

*Yes. requests.Request(method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)
prepare(method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)*


1. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

*`**kwargs` is used to handle named arguments in a function, and it provides a dictionary where the keys are argument names and the values are argument values.
Pros: flexible and easy to extend.
Cons: loss of explicitness and hard to documentation*

1. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

*`None` represents the absence of a value. If arguments are not set to anything, it means the caller must provide this argument while using the method. Other values are used as default values. It could also be set to some default value.*
*Pros of default values: save time and effort of programmers. Make the code extensible.*
