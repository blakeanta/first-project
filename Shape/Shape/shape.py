
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
   
   def DistanceTo(self, new_point):
      pass
   
   def Rotate(self, angle):
      pass
   
   def Scale(self):
      pass


# Shape class inherits from Point
class Shape(ABC, Point):
   
   def __init__(self, type=None):
      self._type = type
      
   def GetShape(self):
      return self._type._Attribute()
   
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
   def _Attribute(cls):
      pass


class Square(Shape):
   '''use Square(p1, p2) or Square(x, y, w, h)'''
   
   def __init__(self, *args):
      super().__init__(Square)
      
      if len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
         self._point_tl = args[0]
         self._point_br = args[1]
         self._side_length = self.GetSideLength()
      
      elif len(args) == 4 and all(isinstance(arg, (int, float)) for arg in args):
         x, y, w, h = args
         self._point_tl = Point(x, y)
         self._point_br = Point(w - x, h - y)
         self._side_length = w

   def GetSideLength(self):
      return self._point_br._x - self._point_tl._x
   
   def Area(self):
      return self._side_length ** 2
   
   def Perimeter(self):
      return 4 * self._side_length
   
   @classmethod
   def _Attribute(cls):
      print("This is a Square")


class Rectangle(Shape):
   pass


class Circle(Shape):
   pass


class Triangle(Shape):
   pass

s = Square(0, 0, 5, 5)
y = Square(Point(1, 2), Point(4, 5))
print(s.Area())
print(y.Area())
