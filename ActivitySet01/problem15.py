# Object Oriented Programming
# https://www.py4e.com/lessons/Objects
class student:
  def __init__(self,name,srn):
    self.name=name
    self.srn=srn
  def display(self):
    print("My name is {0} and srn is {1}".format(self.name,self.srn))
s1=student("nikhil","r21ef238")
s1.display()

#ENCAPSULATION
class Computer:
  '''program to demonstrate Encapsulation'''
  def __init__(self):
    self.__maxprice=900
  def sell(self):
    print("selling price is:",self.__maxprice)
  def setmaxprice(self,price):
    self.__maxprice=price
c1=Computer()
c1.sell( )

#ABSTRACTION
class Polygon:
  def sides(self):
    pass
class triangle(Polygon):
  def sides(self): 
    print("triangle has 3 sides")
class pentagon(Polygon):
  def sides(self):
    print("pentagon has 5 sides")
t=triangle()
t.sides()
p=pentagon()
p.sides()