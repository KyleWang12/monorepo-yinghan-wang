# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- concrete class. It does not extend the ABC class.
2. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- `__del__` is the destructor class. It's called when an instance of Image is about to be destroyed.
3. What class does Texture inherit from?
	- Image
4. What methods and attributes does the Texture class inherit from 'Image'? 
	- `__init__`
	- `getWidth`
	- `getHeight`
	- `getPixelColorR`
	- `getPixels`
	- `setPixelsToRandomValue`
	- `m_width`
	- `m_height`
	- `m_colorChannels`
	- `m_Pixels`
5. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- A texture is not an image, but it can be combined with an image. So it should be 'has-a' relationship.
6. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- No. constructor of Image was called.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

No. If two threads call Logger.instance() at roughly the same time, and _instance is None in both threads, then both threads might end up creating a new instance of Logger. 
  
