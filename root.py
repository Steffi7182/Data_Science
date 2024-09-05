import cmath
a = float(input("Enter number:"))
b = float(input("Enter number:"))
c = float(input("Enter number:"))
d = (b*b) - (4*a*c)
r1 = (-b-cmath.sqrt(d))/(2*a)
r2 = (-b+cmath.sqrt(d))/(2*a)
print(r1,r2)



