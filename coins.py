coins = 0
end_game = False
while end_game < 1:
    coin_total = print('You have %s coins.' % (coins))
    want_more = str(input('Do you want another? (yes or no) '))
    if want_more == 'yes':
        coins += 1
    else:
        print('Bye')
        end_game = True
