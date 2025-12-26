import random

print("== SKIBIDI MATH CONSOLE ==")
print("give correct answers to get scores.")

score = 0

while True:
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    real = a + b

    if random.randint(0, 1) == 1:
        show = real
    else:
        show = real + random.randint(1, 3)

    print(str(a) + " + " + str(b) + " = " + str(show))

    ans = int(input("1 for True, 0 for False: "))

    if show == real and ans == 1:
        score = score + 1
        print("score:", score)
    elif show != real and ans == 0:
        score = score + 1
        print("score:", score)
    else:
        print("noob")
        break

print("== GAME OVER ==")
print("your total score is", score)
