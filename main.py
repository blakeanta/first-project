from package_1 import Function1, Function2, SubPackage1Class, say_hello, add, greet
from Shape.Shape.shape import Polygon, Point


##################################################################################
#  This main.py serve as an entry of the entire program.
#  All program written in this project will be calling from 
#  this file.
#
###################################################################################



def otherFunction():
   print("Other functions")
   callingFunctionFromLearnDecorator()
   Function2()
   Function1()
   obj = SubPackage1Class(__name__)

def callingFunctionFromLearnDecorator():
   say_hello()
   print(add(2, 3))
   greet("Ali")
   print(greet.__name__)
   print(greet.__doc__)


def main():
   print("Hello World")
   otherFunction()
   poly = Polygon((0,0), (3,4), Point(7, 4), (7,0))
   poly.GetPointList()
   print(poly.GetPerimeter())
   
   
   
if __name__ == "__main__":
   main()