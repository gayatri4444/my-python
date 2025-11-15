#inheritance
class book:
  def speak(self):
    print("the pen")

class pen(book):
  def speak(self):
    print("the paper")

obj = book()
obj.speak()
obj1 = pen()
obj1.speak()   
