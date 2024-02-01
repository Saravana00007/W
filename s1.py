import turtle
import math
import json
import re

screen=turtle.Screen()
screen.title("Game")
screen.bgcolor("Green")
screen.setup(width=500,height=500)
screen.tracer(0)

head=turtle.Turtle()
head.color("black")
head.shape("square")
head.speed(0)
head.penup()
head.goto(0,0)
head.direction="stop"

food=turtle.Turtle()
food.color("red")
food.shape("circle")
food.speed(0)
food.goto(0,100)

segment=[]
score=0

a="hi heloo"
print(a[3])
b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[:5])
a = "    Hello, World! "
print(a.strip())
a = "Hello, World!"
print(a.replace("H", "J"))
a = "Hello, World!"
print(a.split(","))
a = "Hello"
b = "World"
c = a + b
print(c)
a = "Hello"
b = "World"
c=a+""+b
print(c)
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
ms="sra"
mt=iter(ms)
print(next(mt))
print(next(mt))
print(next(mt))

class My():
    def _iter_(self):
        self.a=1
        return self
    def _next_(self):
        x=self.a
        self.a  +=1
        return x
def myfunc():
      x = 300
      def myinnerfunc():
          print(x)
          myinnerfunc()
myfunc()
def my():
    x=100
    print(x)
my()
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)
x = abs(-7.25)
print(x)
x=pow(4,3)
print(x)
x=math.sqrt(64)
print(x)
x=math.ceil(1.3)
y=math.floor(4.5)
print(x)
print(y)
x = '{ "name":"John", "age":30, "city":"New York"}'
y=json.dumps(x)
print(y)
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
username = input("Enter username:")
print("Username is: " + username)
arr=np.array([1,2,3,4,54])
print(arr)
print(type(arr))