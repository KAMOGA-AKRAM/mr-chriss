def area_of_circle(radius):
    pi = 3.14159
    return pi * radius *radius

r = float(input('enter the radius of a circle:'))
area = area_of_circle(r)

print('the area of a cirle is:',area)






class circle:
    def __init__(self,radius):
        self.radius = radius


    def area(self):
       return 3.14 * self.radius * self.radius
    

        
    
    # creation of objects
c1 = circle(7)
c2 = circle(6.5)
    
print('the area of circle c1 is', c1.area())