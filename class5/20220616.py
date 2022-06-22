# a = [1, 2, 3]
# b = a
# b[0] = 2
# print(a)
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

juice = ['蘋果汁', '柳橙汁', '葡萄汁']
print(juice[0])
while True:
    print("1.蘋果汁\n2.柳橙汁\n3.葡萄汁\n4.exit")
    ans = input("請輸入果汁編號")
    if ans == "4":
        print("nothing")
    elif ans >= "4":
        print("查無此商品")
    else:
        print(juice[ans - 1])
