#Count digits of a number
x = int(input("enter the number"))
Count=0
while x > 0:
  Count = Count+1
  x=x//10
print("number of digits =",Count)  
