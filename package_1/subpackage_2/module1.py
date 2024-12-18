from functools import wraps

#############################################################################################
#  This module served as the wrapper function source
#  This file is mainly focus on decorator in python.
#
#  In Python, a decorator is a function that allows you to modify the behavior of 
#  another function or class. Decorators are often used for code reuse and separation 
#  of concerns, enabling you to add functionality to existing code in a clean and 
#  maintainable way.
#
#  A decorator is simply a function that takes another function as input, adds some 
#  functionality to it, and returns it. The syntax for applying a decorator is the 
#  @decorator_name line placed above a function.
#  
#  Real-World Use Cases of Decorators:
#  Logging: Automatically log the entry, exit, and result of functions.
#  Access Control: Restrict access based on permissions, often used in web applications.  
#  Caching: Cache the results of expensive function calls for performance.
#  Timing: Measure how long a function takes to execute.
#
#############################################################################################


#############################################################################################
#  simple_decorator is the decorator function.
#  wrapper() adds functionality around say_hello().
#  The @simple_decorator syntax is a shortcut for say_hello = simple_decorator(say_hello).
#
#  def wrapper(*args, **kwargs):
#  *args and **kwargs in the wrapper function ensure that all positional and keyword arguments, 
#  including self, are forwarded correctly to the decorated method.
#  This makes the decorator compatible with any method or function.
#############################################################################################


def simple_decorator(func):
   def wrapper(*args, **kwargs):
      print("Function is about to run")
      func(*args, **kwargs)
      print("Function has finished running")
   
   # Remark: Must return wrapper to avoid TypeError
   return wrapper


def decorator_with_args(func):
   def wrapper(*args, **kwargs):
      print("Arguments", args, kwargs)
      result = func(*args, **kwargs)
      return result
   return wrapper

#############################################################################################
#  Using functools.wraps
#  To preserve the original function’s metadata (like its name and docstring) 
#  when using decorators, it’s a good practice to use functools.wraps:
#
##############################################################################################

def built_in_wraps(func):
   # Preserves the original function's metadata
   @wraps(func)
   def wrapper(*args, **kwargs):
      print("Wrapper called")
      return func(*args, **kwargs)
   return wrapper

