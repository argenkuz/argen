
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
