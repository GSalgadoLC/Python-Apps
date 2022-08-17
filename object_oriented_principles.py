from abc import ABC

# Encapsulation - variable protection


class Alpha:

    def __init__(self):
        self._a = 2.  # Protected member ‘a’
        self.__b = 2.  # Private member ‘b’

# Inheritance


class Parent:
    b = 1
    # Members of the parent class


class Child(Parent):

    a = 1
    # Inherited members from parent class
    # Additional members of the child class


# Abstraction
# "abc" here stands for abstract base class. It is
# first imported and then used as a parent class for
# some class that becomes an abstract class. Its simplest
#  implementation can be done as below.

# Line 1
class ClassName(ABC):
    pass


#Classes and instances

class MyClass:
    print("Hello")


myc = MyClass()


class MClass:
    a = 5
    print("Hello")

    def hello(self):
        print("Hello world")


ayc = MClass()
print(MClass.a)
print(ayc.a)
print(ayc.hello())
