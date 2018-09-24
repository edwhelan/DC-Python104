#how big is the square
square_size = int(input('How big is the square? '))
counterY = 0
#build out square
while counterY < square_size:
    counterX = 0
    while counterX < square_size:
        print('*', end='')
        counterX += 1
    print()
    counterY += 1