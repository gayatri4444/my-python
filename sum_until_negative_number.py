#sum until negative number
sum = 0
while True:
 n = int(input("enter the number"))
 if n < 0:
    break
 sum = sum + n
print("Sum =",sum)
