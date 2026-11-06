area=lambda length, width:length*width
print(area(12,10))

add= lambda x: x+10
print(add(5))

people= lambda family:family+6
print(people(7))

strength=lambda power: "Enter" if power>50 else "Too weak"
print(strength(65))

Sqr=lambda y:y**2
print(Sqr(7))
import math
radius= lambda j:math.pi *j**2
print(radius(7))

def multiplier(n):
    return lambda a:a*n
doubler=multiplier(2)
tripler=multiplier(3)
print(doubler(20))
print(tripler(20))

