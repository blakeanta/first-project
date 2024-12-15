import learn_decorator


##################################################################################
#  This main.py serve as an entry of the entire program.
#  All program written in this project will be calling from 
#  this file.
#
###################################################################################



def otherFunction():
   print("Other functions")
   callingFunctionFromLearnDecorator()

def callingFunctionFromLearnDecorator():
   learn_decorator.say_hello()
   print(learn_decorator.add(2, 3))
   learn_decorator.greet("Ali")
   print(learn_decorator.greet.__name__)
   print(learn_decorator.greet.__doc__)


def main():
   print("Hello World")
   otherFunction()
   
   
   
   
if __name__ == "__main__":
   main()