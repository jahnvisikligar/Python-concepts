## OOP(Object-Oriented programming):

### Class

A class is a collection of objects. It contains blueprints/prototypes from which the objects are being created. It is a logical entity that contains some attributes and methods. A class instance with a defined set of properties is called an object. As a result, the same class can be used to construct as many objects as needed. The `__init__` special method also known as a constructor is used to initialize the 'Class Name' class with attributes. 

In the provided code example: 

      class Book:
        def __init__(self,title,author,price) -> None:
          self.title=title
          self.author=author
          self.__price=price

* class = Book
* attributes = title, author, price

The built-in classes are named in lowercase for the `__init__` method. The user-defined classes are Camel case or Snake case. The special method is defined which begins and ends with two underscores and is invoked automatically when certain conditions are met.
>Attributes are names given to variables contained in a class.

### Encapsulation

It prevents clients from accessing certain properties, which can only be accessed through specific methods. Information hiding is the process of making particular attributes private. Encapsulation is done by adding two underscores before the attribute name. In the provided example it is achieved in the `__discount` attribute in class 'Book'. The function of the `set_discount` method is to assign the `__discount` attribute and the `get_Price` method computes the final price after pushing the 'discount' attribute. The code for computing the final price after implementing the discount goes as follows:

    class Book(ABC):
      def __init__(self,title,author,price) -> None:
        self.title=title
        self.author=author
        self.price=price
        self.__discount=None
      def set_discount(self,discount):
        self.__discount=discount
      def get_Price(self):
        if self.__discount:
          return (self.price*(1-self.__discount))
        return self.price

>Private attributes are inaccessible attributes

### Inheritance

An inheritance is a class's ability to inherit methods/characteristics from another class.                    

Continuing the above example, adding the 'Novel' class has the same attributes such as title, author, and price as the parent class Book. The implemented code example for the same is shown below:

    class Novel(Book):
      def __init__(self, title, author, price,genre) -> None:
        super().__init__(title, author, price)
        self.genre=genre

>`Parent/Super class ---(inherits attributes/methods)---> sub/child class`
       
### Polymorphism

It refers to a sub-class's ability to adapt a method that already exists in its super class to meet its needs. There are two ways to implement it:
* The first method involves taking the attributes of the parent class as they are.
* In the second approach, there is invoking of its own method by suppressing the same method present in its super class

The example provided below the `__repr__` method of the 'Novel' class supersedes the `__repr__` method of the parent class 'Book'. The code is as shown below  :

    class Novel(Book):
      def __init__(self, title, author, price,genre) -> None:
        super().__init__(title, author, price)
        self.genre=genre
      def __repr__(self):
        return f"""Novel:{self.title},Author:{self.author},Price:{self.get_Price()},Genre:{self.genre}"""
### Abstraction
Abstraction is a process of handling complexity by hiding unnecessary information from the user. It enables the user to implement even more complex logic on top of the provided abstraction without understanding or even thinking about the hidden background/back-end complexity. An abstract method is a method that is declared but does not contain implementation. It identifies the functionality that should be implemented by all its sub-classes.

>Abstraction allows a programmer to hide all irrelevant data/processes of an application to reduce complexity and increase the efficiency of the programme.
>Implementation would differ from one subclass to another. It sometimes comprises of `pass` statement
>Not directly supported in python
>Need to class `ABC`(Abstract Base Class) for implementation as follows:

`from abc import ABC abstractmethod`

Given in the provided example abstraction has been achieved as follows:

Syntax:

      from abc import ABC
      class ClassName(ABC):

Implementation:

      from abc import ABC, abstractmethod
      class Book(ABC):
        def __init__(self,title,author,price) -> None:
          self.title=title
          self.author=author
          self.__price=price
          self.__discount=None
        def set_discount(self,discount):
          self.__discount=discount
        def get_Price(self):
          if self.__discount:
            return (self.__price*(1-self.__discount))
          return self.__price
        @abstractmethod
        def __repr__(self):
          return f"""Book:{self.title},Author:{self.author},Price:{self.get_Price()}"""
It is to be noted that with abstraction, the Novel class is forced to have its own `__repr__` method as opposed to the process of Polymorphism and Encapsulation. 

### Method Overriding

* Method with the same name and arguments is used both in a derived class and a base class/super class. It is said that the derived class 'overrides' the method provided in a base class.
* When the overridden method gets called, the derived class's method is always invoked.
* To invoke the method from the Parent class, use the keyword `super`

### Method Overloading

It refers to the use of many methods with the same name that take different numbers of arguments within a single class.




