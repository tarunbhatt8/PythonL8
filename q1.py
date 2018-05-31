''' Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class. '''
import math as m
class Circle:
        '''class to get area and circumference of a circle using the radius'''

        def __init__(self,r):
            self.radius=r

        def getArea(self):
            '''method to get area of the circle'''
            return m.pi*((self.radius)**2)

        def getCircumference(self):
            '''method to get circumference of the circle'''
            return 2*(m.pi)*self.radius

r=float(input("Enter radius of circle: "))
c1=Circle(r)
print("Radius={} Area={} Circumference={}".format(c1.radius,c1.getArea(),c1.getCircumference()))
