1. __init__ (Constructor) 
Runs automatically when an object is created.
Used to initialize (set up) the object's data.

Example:

def __init__(self, name):
    self.name = name


2. Instance Variables
Created using self.variable.
Each object has its own copy.

Example:
self.name = name



3. Class Variables
Belong to the class.
Shared by all objects unless an object creates its own variable with the same name.




4. Attribute Lookup Order

When you write:
obj.attribute

Python checks:
The object (instance).
The class.
Otherwise, raises AttributeError.

Remember: Instance first, Class second.


5. self
Refers to the current object.
Python automatically passes it when you call an instance method.
obj.method()

becomes internally:
Class.method(obj)



6. Instance Methods

Methods that work with a specific object and usually use self to access that object's data.



7. print() vs return
print() → Displays the value on the screen.
return → Sends the value back to the caller so it can be stored or used later.

Golden Rule:
Want to show something? → print()
Want to use the result later? → return
