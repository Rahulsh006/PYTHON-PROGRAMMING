
from mypackage import circle,rectangle
from mypackage.graphics_3d import sphere
from mypackage.graphics_3d.cuboid import *


r=float(input("enter radius:"))

ca=circle.area(r)
print("area of circle=",ca)
cp=circle.perimeter(r)
print("perimeter of circle=",cp)

l=float(input("enter length:"))
b=float(input("enter breadth:"))


ra=rectangle.area(l,b)
print("area of rectangle=",ra)
rp=rectangle.perimeter(l,b)
print("perimeter of rectangle=",rp)

r=float(input("enter radius of sphere:"))

sa=sphere.area(r)
print("area of sphere=",sa)
sv=sphere.volume(r)
print("volume of sphere=",sv)

length=float(input("enter length of cuboid:"))
breadth=float(input("enter breadth of cuboid:"))
height=float(input("enter height of cuboid:"))
weight=float(input("enter weight of cuboid:"))

ca=area(length,weight,height)
print("area of cuboid=",ca)
cp=perimeter(length,breadth,height)
print("perimeter of cuboid=",cp)
