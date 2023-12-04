



import random
def int_validation(x):
    x = input(f"{x}")
    try:
        x = int(x)
        if x > 7 or x < 1:
            print("invalid input")
        else:
            return x
    except ValueError:
        print("wrong input")
        return 0
killometres = [711,0,0,0,1,1,0]
game = True
while game:
    print(killometres)
    summ = 0
    for _ in range(3):
        summ += killometres[int_validation("select killometr: ") - 1]
    if summ == 713:
        print("You've won!")
        game = False
    else:
        print("wrong! Tentacles changed position of boxes.Try again")
        random.shuffle(killometres)
