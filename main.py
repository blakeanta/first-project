from package_1 import Function1, Function2, SubPackage1Class, LearnDecorator
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
   Function2()
   Function1()
   callingFunctionFromLearnDecorator()
   obj = SubPackage1Class(__name__)

def callingFunctionFromLearnDecorator():
   obj = LearnDecorator(__name__)
   obj.say_hello()
   print(obj.add(2, 3))
   print(obj.add(1, 5, 8))
   obj.greet("Ali")
   print(obj.greet.__name__)
   print(obj.greet.__doc__)
   
def callingFunctionFromShape():
   square = Square(10, 0, 6, 6)
   print(square._point_br._x)
   print(square._point_br._y)
   


def main():
   print("Hello World")
   otherFunction()
   
  
   
   
   
if __name__ == "__main__":
   main()