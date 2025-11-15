#multi inheritance
class a:
  def fun1(self):
    print("i am good")

class b:
  def fun2(self):
    print("i am not good")    
class C(a,b):
  print("everything is ok")

obj1 = a()
obj1.fun1()   
obj2 = b()
obj2.fun2()
