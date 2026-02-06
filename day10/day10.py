# import os

# BASE_DIR = os.path.dirname(__file__)
# path = os.path.join(BASE_DIR, "myText.txt")

# with open(path, "r", encoding="utf-8") as file:
#     for i, line in enumerate(file, start=1):
#         print(f"{i}. {line.strip()}")



# n = int(input("Nhap so dong n: "))

# lines = []

# for i in range(1, n + 1):
#     text = input(f"Nhap dong thu {i}: ")
#     lines.append(f"{i}. {text}\n")

# file = open("myText.txt", "w", encoding="utf-8")
# file.writelines(lines)
# file.close()



# def append_text_to_file():
#     myListText = []

#     n = int(input("Nhap so luong phan tu muon ghi: "))

#     for i in range(0, n):
#         value = input(f"Nhap dong thu {i + 1}: ")
#         addDropLine = value + "\n"
#         myListText.append(addDropLine)

#     file = open("myText.txt", "a", encoding="utf-8")
#     file.writelines(myListText)
#     file.close()



# append_text_to_file()

# bai1
# file = open("myText.txt", "r")
# lines = file.readlines()
# file.close()

# print("list of names:")

# for line in lines:
#     name = line.strip()
#     if name != "":
#         print("- " + name)

# bai2
# filename = input("input file name: ")

# try:
#     file = open(filename, "r")
#     content = file.read()
#     file.close()

#     print("file content:")
#     print(content)

# except:
#     print("file not found.")

# bai3
# file = open("user-inputs.txt", "w")

# print("== input file content below ==")

# while True:
#     line = input()
#     if line == "":
#         break
#     file.write(line + "\n")

# file.close()

# print("== input recorded in user-inputs.txt ==")

# bai4
# from datetime import datetime

# file = open("input-logs.txt", "a")

# time_now = datetime.now()

# file.write("== inputs at " + str(time_now) + " ==\n")

# print("== input file content below ==")

# while True:
#     line = input()
#     if line == "":
#         break
#     file.write(line + "\n")

# file.write("\n")
# file.close()

# print("== input recorded in input-logs.txt ==")

# bai5
file = open("question-bank.txt", "r")
lines = file.readlines()
file.close()

score = 0
total = 0

print("give the correct answers to get points.")

for line in lines:
    line = line.strip()

    if line == "":
        continue

    parts = line.split(",")
    question = parts[0]
    answer = parts[1]

    user = input(question)

    if user == answer:
        score = score + 1

    total = total + 1

print("== you get " + str(score) + "/" + str(total) + " points ==")
