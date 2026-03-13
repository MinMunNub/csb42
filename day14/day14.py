# p1
# # b1
# kho = {
#     "HP": 20,
#     "DELL": 50,
#     "MACBOOK": 12,
#     "ASUS": 30
# }

# # b2
# print("available MACBOOKs:", kho["MACBOOK"])

# # b3
# hang = input("input a brand: ")
# print("available", hang + "s:", kho[hang])

# p2
# # data from part 1
# kho = {
#     "HP": 20,
#     "DELL": 50,
#     "MACBOOK": 12,
#     "ASUS": 30
# }

# # b1
# kho["TOSHIBA"] = 10
# print("available products:")
# for i in kho:
#     print("-", i + ":", kho[i])

# # b2
# brand = input("input a brand: ")
# amount = int(input("input amount: "))
# kho[brand] = amount

# print("available products:")
# for i in kho:
#     print("-", i + ":", kho[i])

# # b3
# kho["DELL"] = 60
# kho["MACBOOK"] = 2

# print("available products:")
# for i in kho:
#     print("-", i + ":", kho[i])

# # b4
# tong = 0
# for i in kho:
#     tong = tong + kho[i]

# print("total products:", tong)

# p3
# # b1
# price = {
#     "HP": 600,
#     "DELL": 650,
#     "MACBOOK": 1200,
#     "ASUS": 400
# }

# # b2
# print("Price of ASUS:", price["ASUS"])

# # b3
# brand = input("Input a brand: ")
# print("Price of", brand + ":", price[brand])

# p4
# price = {
#     "HP": 600,
#     "DELL": 650,
#     "MACBOOK": 1200,
#     "ASUS": 400
# }

# stock = {
#     "HP": 20,
#     "DELL": 50,
#     "MACBOOK": 12,
#     "ASUS": 30
# }

# # b1
# print("total price:", price["ASUS"] * 5)

# # b2
# brand = input("input a brand: ")
# amount = int(input("input amount to buy: "))
# print("total price:", price[brand] * amount)

# # b3
# brand = input("input a brand: ")
# amount = int(input("input amount to buy: "))
# total = price[brand] * amount
# print("total price:", total)

# stock[brand] = stock[brand] - amount

# print("available products:")
# for i in stock:
#     print("-", i + ":", stock[i])

# p5
# price = {
#     "HP": 600,
#     "DELL": 650,
#     "MACBOOK": 1200,
#     "ASUS": 400
# }

# stock = {
#     "HP": 20,
#     "DELL": 50,
#     "MACBOOK": 12,
#     "ASUS": 30
# }

# # b1
# print("total value of available brands:")
# for i in stock:
#     value = stock[i] * price[i]
#     print("-", i + ":", value)

# # b2
# total = 0
# for i in stock:
#     total = total + stock[i] * price[i]

# print("total value of available items:", total)

# p6
# # b1
# player = {
#     "Name": "Light",
#     "Age": 17,
#     "Strength": 8,
#     "Defense": 10,
#     "HP": 100,
#     "Backpack": ["Shield", "Bread Loaf"],
#     "Gold": 100,
#     "Level": 2
# }

# # b2
# player["Gold"] = player["Gold"] + 50
# print("Gold:", player["Gold"])

# # b3
# player["Backpack"].append("FlintStone")
# print("Backpack:", ", ".join(player["Backpack"]))

# p7
# # b1
# skills = [
#     {"Name": "Tackle", "Minimum level": 1, "Damage": 5, "Hit rate": 0.3},
#     {"Name": "Quick Attack", "Minimum level": 2, "Damage": 3, "Hit rate": 0.5},
#     {"Name": "Strong Kick", "Minimum level": 4, "Damage": 9, "Hit rate": 0.2}
# ]

# # b2
# for i in range(len(skills)):
#     print("skill", i+1, ":", skills[i]["Name"])

# p8
import random

level = 2

skills = [
    {"Name": "Tackle", "Minimum level": 1, "Damage": 5, "Hit rate": 0.3},
    {"Name": "Quick Attack", "Minimum level": 2, "Damage": 3, "Hit rate": 0.5},
    {"Name": "Strong Kick", "Minimum level": 4, "Damage": 9, "Hit rate": 0.2}
]

for i in range(len(skills)):
    print("skill", i+1, ":", skills[i]["name"])

n = int(input("choose skill by number: "))
s = skills[n-1]

print("you chose", s["Name"] + ".")

if level < s["minimum level"]:
    print("cannot deploy. Required level", s["minimum level"])
else:
    r = random.random()
    if r <= s["hit rate"]:
        print("damage:", s["damage"])
    else:
        print("missed.")