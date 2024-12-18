from package_1 import Function1, Function2, SubPackage1Class, say_hello, add, greet
from Shape import Square, Rectangle, Triangle, Circle



##################################################################################
#  This main.py serve as an entry of the entire program.
#  All program written in this project will be calling from 
#  this file.
#
###################################################################################



def otherFunction():
   print("Other functions")
   callingFunctionFromShape()
   callingFunctionFromLearnDecorator()
   Function2()
   Function1()
   obj = SubPackage1Class(__name__)
   callingFunctionFromShape()

def callingFunctionFromLearnDecorator():
   say_hello()
   print(add(2, 3))
   greet("Ali")
   print(greet.__name__)
   print(greet.__doc__)
   
   
def callingFunctionFromShape():
   circle = Circle(1, 2, diameter= 5)
   circle.GetShape()
   print(circle.Area())
   square = Square(10, 0, 6, 6)
   print(square._point_br._x)
   print(square._point_br._y)
   


def main():
   print("Hello World")
   otherFunction()
   
  
   
   
   
if __name__ == "__main__":
   main()