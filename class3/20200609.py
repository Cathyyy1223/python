#score = int(input("score:"))
#if score >= 90:
#print("優等")
#elif score >= 80:
#print("甲等")
#elif score >= 70:
#print("乙等")
#elif score >= 60:
#print("丙等")
#elif score <= 59:
#print("丁等")
#import numbers

#number = int(input("NUMBER:"))
#if number % 2 == 0:
#print("偶數")
#if number % 2 != 0:
#print("奇數")

import turtle

#turtle.forward(100)
#turtle.backward()
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.done()
# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)
turtle.color("purple")
turtle.shape("circle")
turtle.penup()
for i in range(4, 200, 4):
    turtle.forward(30 + i)
    turtle.right(25 + i)
    turtle.stamp()
turtle.done()