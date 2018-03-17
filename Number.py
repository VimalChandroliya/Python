#NUmbers

a=2
b=3
#comparison < > == !=
print("is a=b?" , a==b)
print("is A!=b" , a!=b)

#assignment
b += a
print(b)

#Logical  and or not
x = True
y = False
print("x and y" , x and y)
print("x or y" , x or y)
print("not of x", not x)
print("not of y", not y)

#bitwise | & ^
a = 6 #110
b = 2 #010
print("Bitwise and = " , a & b)
print("Bitwise or = ",a | b)
print("Bitwise xor = ",a ^ b)

print("a>>b = " , a>>b)
print("a<<b = ",a<<b)

#identity is is not
print("a is 6 ", a is 6)
print("a is not 6 ",a is not 6)

#memebrship operator in not in
x = [1,2,3,4]
print("3 in x ", 3 in x)
print("3 not in x", 3 not in x)
