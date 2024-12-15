
def Function1():
   print(f"{Function1.__name__} from {__name__}")
   obj = SubPackage1Class(__name__)
   
class SubPackage1Class:
   def __init__(self, name):
      self.name = name
      print(f"{SubPackage1Class.__name__} is instantiate from {self.name}")
