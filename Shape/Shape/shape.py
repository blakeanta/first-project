from math import sqrt
from abc import ABC, abstractmethod



#################################################################
#
# This file is mainly focus on classes of shape 
#
# To create a base class in Python that can only be used for 
# inheritance (and not instantiated directly), you can use an 
# abstract base class (ABC). Abstract base classes define a 
# common interface for subclasses but prevent direct 
# instantiation of the base class.
# Instantiation: If you try to instantiate BaseClass directly, 
# Python will raise a TypeError, because abstract classes cannot 
# be instantiated.
# Trying to create an instance of BaseClass will raise an error:
# base = BaseClass()  # This will raise TypeError: Can't 
# instantiate abstract class
#################################################################


########################################################
# Start with the base class then followed by othe shape
########################################################

# This class will represent a point in 2D space with x and y coordinates.
class Point:
   def __init__(self, x, y):
      self._x = x
      self._y = y

   def __repr__(self):
      return f"Point({self._x, self._y})"
   
   def DistanceTo(self, new_point: "Point"):
      if not isinstance(new_point, Point):
         raise TypeError("new_point must be an instance of Point")
      distance = sqrt()
   
   
   def Rotate(self, angle):
      pass
   
   def Scale(self):
      pass


# Shape class inherits from Point
class Shape(ABC, Point):
   
   def __init__(self, x, y, remark=None):
      super().__init__(x, y)
      self._remark = remark
      
   # Abstract method: Must be implemented by any subclass
   # @abstractmethod: This decorator marks the method as abstract, 
   # meaning that any subclass must implement it.
   @abstractmethod
   def Area(self):
      '''Calculate the area of the shape'''
      pass
   
   @abstractmethod
   def Perimeter(self):
      '''Calculate the perimeter of the shape'''
      pass
   
   def Rotate(self, angle):
      """Rotate the shape around its position by the given angle."""
      # Rotate the center of the shape (the point) around the origin
      new_center = self.Rotate(angle)
      return new_center
      
   def Scale(self):
      """Scale the shape by the given factor."""
      # Scale the dimensions of the shape (e.g., radius, width, height, side_length)
      self.Scale()
      
   # An abstractclassmethod is a special kind of abstract method that 
   # is a class method, meaning it’s a method bound to the class rather
   # than an instance. It works similarly to an abstract method but 
   # specifically for class methods.
   # To define an abstract class method, use both the @abstractmethod 
   # decorator and the @classmethod decorator. This means that subclasses 
   # must implement the class method.
   @classmethod
   @abstractmethod
   def Attribute(cls):
      pass


class Square(Shape):
   def __init__(self, x, y, side_length=None, remark=None):
      super().__init__(x, y, remark)
      self._side_length = side_length

   def Area(self):
      return self._side_length ** 2
   
   def Perimeter(self):
      return 4 * self._side_length
   
   @classmethod
   def Attribute(cls):
      print("This is a Square")


class Rectangle(Shape):
   pass


class Circle(Shape):
   pass


class Triangle(Shape):
   pass


Square.Attribute()
