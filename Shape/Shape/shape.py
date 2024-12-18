import math
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
   
   def _DistanceTo(self, pt1: "Point", pt2: "Point"):
      """Calculate the Euclidean distance between two points."""

      if not (isinstance(pt1, Point) and isinstance(pt2, Point)):
         raise TypeError("new_point must be an instance of Point")
      
      distance = math.sqrt((pt1._x - pt2._x) ** 2 + (pt1._y - pt2._y) ** 2)
      return distance
   
   def Rotate(self, angle):
      """Rotate the point around the origin (0, 0) by the given angle in degrees."""
      angle_rad = math.radians(angle)
      new_x = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
      new_y = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
      return Point(new_x, new_y)
      
   
   def Scale(self, factor):
      """Scale the point by the given factor."""
      return Point(self.x * factor, self.y * factor)


# Shape class inherits from Point
class Shape(ABC, Point):
   
   def __init__(self, shape_type=None):
      self._type = shape_type
      
   def GetShape(self):
      return self._type._Attribute()
   
   # Abstract method: Must be implemented by any subclass
   # @abstractmethod: This decorator marks the method as abstract, 
   # meaning that any subclass must implement it.
   @abstractmethod
   def GetArea(self):
      '''Calculate the area of the shape'''
      pass
   
   @abstractmethod
   def GetPerimeter(self):
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
   '''Create instance with Square(p1, p2) where p1 is top left point and p2 is bottom right 
   or Square(x, y, w, h) where x and y is top left corner and w and h is width and height'''
   
   def __init__(self, *args):
      super().__init__(Square)
      
      if len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
         self._point_tl = args[0]
         self._point_br = args[1]
         self._side_length = self.CalSideLength()
      
      elif len(args) == 4 and all(isinstance(arg, (int, float)) for arg in args):
         x, y, w, h = args
         
         if w != h:
            raise ValueError("This is not a square. Width and height should be same value")
         
         self._point_tl = Point(x, y)
         self._point_br = Point(x + w, y + h)
         self._side_length = w

   def CalSideLength(self):
      w = self._point_br._x - self._point_tl._x
      h = self._point_br._y - self._point_tl._y
      
      if abs(w) != abs(h):
         raise ValueError("This is not a square. Width and height should be same value")

      return w
   
   def GetArea(self):
      return self._side_length ** 2
   
   def GetPerimeter(self):
      return 4 * self._side_length
   
   @classmethod
   def _Attribute(cls):
      print("This is a Square")


class Rectangle(Shape):
   pass


class Circle(Shape):
   '''Create instance of Circle with Circle(x, y, diamter=) or Circle(x, y, radius=) or Circle(Point, radius=), 
   where x and y is center of the circle '''
   
   def __init__(self, *args, diameter=None, radius=None):
      super().__init__(Circle)
      
      if len(args) == 2 and all(isinstance(arg, (int, float)) for arg in args):
         self._center_point = Point(args[0], args[1])
      
      elif len(args) == 1 and isinstance(args[0], Point):
         self._center_point = args[0]
         
      else:
         raise ValueError("Too many arguments or wrong type is provided")
         
         
      if diameter is not None:
         self._diameter = diameter
         self._radius = self._diameter / 2
         
      elif radius is not None:
         self._radius = radius
         self._diameter = self._radius * 2
         
      else:
         raise ValueError("diameter and radius cannot be both None must be provided one of them")
      
      
      
   def Area(self):
      return math.pi * (self._radius ** 2)
   
   def Perimeter(self):
      return 2 * math.pi * self._radius
   
   @classmethod
   def _Attribute(cls):
      print("This is a circle")


class Triangle(Shape):
   pass


class Polygon(Shape):
   '''Instantiate Polygon with at least 3 Point. Polygon(p1, p2, p3) or Polygon((x1, y1), (x2, y2), (x3, y3)) 
   or Polygon(p1, (x1, y1), p2, p3, (x2, y2))'''

   def __init__(self, *args):
      super().__init__(Polygon)
      self._point_list = list()
      
      if len(args) < 3:
         raise ValueError("Polygon must have at least 3 points")
      
      for arg in args:
         if isinstance(arg, Point):
            self._point_list.append(arg)
         
         elif isinstance(arg, tuple) and len(arg) == 2 and all(isinstance(item, (int, float)) for item in arg):
            new_point = Point(arg[0], arg[1])
            self._point_list.append(new_point)
         
         else:
            raise ValueError("Wrong argument type. Arguments must be either Point or tuple of float or int or both.")
         
         
   def GetPointList(self):
      for point in self._point_list:
         print(f"({point._x}, {point._y})")
         
      return self._point_list
   
   def GetArea(self):
      """This feature is not yet developed"""
      pass
   
   def GetPerimeter(self):
      res = 0
      l, r = 0, 1
      
      while l < r:
         res += self._DistanceTo(self._point_list[l], self._point_list[r])
         l += 1
         r += 1
         
         if r >= len(self._point_list):
            r = 0
            res += self._DistanceTo(self._point_list[l], self._point_list[r])
            return res
   
   @classmethod
   def _Attribute(cls):
      print("This is a Polygon")
      

