from .module1 import simple_decorator, decorator_with_args, built_in_wraps


#############################################################################################
# This module will be the main implementation of LearnDecorator class
#############################################################################################


class LearnDecorator:
   
   def __init__(self, name):
      self.name = name
      
      print(f"Instantiate an instant of {LearnDecorator.__name__} from {name}")
         
   @simple_decorator
   def say_hello(self):
      print("Hello")
   
   @decorator_with_args
   def add(self, *args):
      res = 0
      for arg in args:
         res += arg
      return res
   
   @built_in_wraps
   def greet(self, name):
      """Greet a person with their name."""
      print(f"Hello, {name}")
   
   


