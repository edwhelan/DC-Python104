banner = input('Text? ')
the_width = len(banner) + 4
height = 0
while height < 3:
    if height == 0 or height == 2:
        print('*' * the_width)
        height += 1
    else:
        print('*' + ' ' + banner + ' ' + '*')
        height += 1