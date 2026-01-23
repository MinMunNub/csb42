# # p1
# # 1.
# colors = ["blue", "red", "green"]

# # 2.
# print("colors list: ", colors)

# # 3.
# new = input("enter new color: ")
# colors.append(new)
# print(colors)

# # p2
# # 1.
# colors = ["blue", "red", "green"]
# pos = int(input("input position: "))
# print("colors at pos: ", pos, ":", colors[pos-1])

# # 2.
# x = input("color to delete: ")
# if x.isdigit():
#     colors.pop(int(x)-1)
# else:
#     colors.remove(x)

# print("new color list:", colors)

# # 3.
# import turtle as t

# turtlecolors = ["blue", "red", "green", "yellow", "orange", "violet"]

# for c in turtlecolors:
#     t.color(c)
#     t.forward(50)
#     t.penup()
#     t.forward(10)
#     t.pendown()

# t.done()

# # p3
# # 1.
# nums = [5, 1, 8, 90, -1, 30]
# x = int(input("input a number: "))
# if x in nums: 
#     print("number found at position", nums.index(x)+1)
# else: 
#     print("number not found")

# # 2.
# nums = [5, 1, 8, 90, -1, 30]
# print("sum of all numbers: ", sum(nums))

# # 3.
# nums = []
# while True:
#     x = int(input())
#     if x == 0:
#         break
#     nums.append(x)

# print("sum of numbers: ", sum(nums))

# # p4
# # 1.
# nums = [5, 1, 8, 92, 7, 30]
# evens = [n for n in nums if n % 2 == 0]
# print("even numbers:", evens)

# # 2.
# nums = []
# while True:
#     x = int(input())
#     if x == 0: break
#     nums.append(x)
# evens = [n for n in nums if n % 2 == 0]
# print("even numbers in list:", evens)

# # p5
# # 1.
# names = ["BD", "BT", "CG", "DD", "HBT"]
# pops = [247100, 333300, 266800, 428900, 318000]
# print(names)
# print(pops)

# # 2.
# names = ["BD", "BT", "CG", "DD", "HBT"]
# pops = [247100, 333300, 266800, 428900, 318000]

# max_i = pops.index(max(pops))
# min_i = pops.index(min(pops))

# print("most populated district: ", max_i)
# print("least populated district: ", min_i)

# # 3.
# names = ["BD", "BT", "CG", "DD", "HBT"]
# pops = [247100, 333300, 266800, 428900, 318000]

# max_i = pops.index(max(pops))
# min_i = pops.index(min(pops))

# print("most populated district name: ", names[max_i])
# print("least populated district name: ", names[min_i])

# # p6
# # 1.
# names = ["BD", "BTL", "CG", "DD", "HBT"]
# areas = [9.224, 43.35, 12.04, 9.96, 10.09]
# pops  = [247100, 333300, 266800, 420900, 318000]

# densities = [pops[i] / areas[i] for i in range(len(names))]

# for i in range(len(names)):
#     print(names[i], densities[i])

# # 2.
# avg = sum(densities) / len(densities)
# print("avg population density: ", avg)

# # p7
# # 1.
# scores = [78, 56, 67]
# print(scores)

# # 2.
# scores = [78, 56, 67]
# print("high score: ")
# for i, s in enumerate(scores, 1):
#     print(i, s)

# # 3.
# scores = [78, 56, 67]
# x = int(input("input new score: "))
# scores.append(x)

# print("high score: ")
# for i, s in enumerate(scores, 1):
#     print(i, s)

# # p8
# # 1.
# scores = [78, 56, 67]
# x = int(input("input new score: "))
# scores.append(x)
# scores.sort(reverse=True)

# print("high score: ")
# for i, s in enumerate(scores, 1):
#     print(i, s)

# # 2.
# scores = [78, 70, 67, 56, 45]
# x = int(input("input new score: "))
# scores.append(x)
# scores.sort(reverse=True)

# top5 = scores[:5]

# print("high score: ")
# for i, s in enumerate(top5, 1):
#     print(i, s)

# danh phuong skibidi