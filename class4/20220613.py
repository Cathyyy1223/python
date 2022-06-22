# import turtle

# turtle.pensize(5)
# turtle.pencolor("blue")
# turtle.fillcolor("purple")
# turtle.begin_fill()
# for i in range(5):
#     turtle.forward(200)
#     turtle.right(144)
# turtle.end_fill()

# i = 0
# in_max = int(input("輸入數值:"))
# sum = 0
# while i <= in_max:
#     print(i)
#     i += 1
#     sum += i

# print(sum)
# while True:
#     print("1.蘋果汁\n2.柳橙汁\n3.葡萄汁\n4.exit")
#     ans = input("請輸入果汁編號")
#     if ans == "4":
#         break
#     elif ans == "1":
#         print("蘋果汁")
#     elif ans == "2":
#         print("柳橙汁")
#     elif ans == "3":
#         print("葡萄汁")
#     else:
#         print("查無此商品")
import random

# print(random.randrange(3))
# print(random.randrange(0, 10, 2))
# random.randint(1,3)
# random.randint(1,10)
ans = random.randint(1, 100)
while True:
    number = int(input('number:'))
    if number > ans:
        print("再大一點")
    if number < ans:
        print("再小一點")