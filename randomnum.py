import random
sec_num = random.randint(1,500)
print("Select any number between 1 and 500\n")

while True:
    res =input("Please Guess the number \n")
    if res == sec_num:
        print("You won ")
        break
    else:
        print("You Lost....Hahaha")
        continue

