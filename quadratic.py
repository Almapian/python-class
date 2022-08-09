#quadratic equation 
a = int(input("enter number for a here: "))
b = int(input("enter number for b here: "))
c = int(input("enter number for c here: "))
d = ((b**2)-4*a*c)**0.5
x1 = (-b + d) / (2*a)
x2 = (-b - d) / (2*a)
print(str(x1) + ", " + str(x2))