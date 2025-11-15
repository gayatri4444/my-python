#Encapsulation
class pen:
  def __init__(self):
    self.public = "i am public"
    self.__private = "i am not public"
  def fun(self):
    print(self.__private)
    print(self.public)
obj = pen()
obj.fun()    
