# colision de dos esferas

from math import sqrt
def funcionball(x,y,r,x1,y1,r1):
    # raizde=(x1-x)^2+(y1-y)^2
    return sqrt((x1-x)**2+(y1-y)**2)





x=float(input("Write x posicion of sphere 1 " ))
y=float(input("write y posicion of sphere 1 " ))
r=float(input("Write the radius of sphere  #1 " ))
x1=float(input("Write x posicion of sphere 2 " ))
y1=float(input("Write y posicion of sphere 2  " ))
r1=float(input("Write the radius of sphere  #2 " ))

esfera1=(x,y,r)
esfera2=(x1,y1,r1)

print ("Data sphere 1",esfera1)
print ("Data sphere 1",esfera2)

# Formula para hallar el centro de dos puntos
# raizde=(x1-x)^2+(y1-y)^2

d=funcionball(x,y,r,x1,y1,r1)
print(d)
rtotal=r+r1
booleano=True if d<=rtotal else False

if booleano:
 print("TRUE")
else :
   print("FALSE")


