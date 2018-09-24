user_num = int(input('Please input a number to be converted '))
counter_num = 1
#take largest number divise into 1 + 1 and while loop
while counter_num <= user_num:
    if user_num % counter_num == 0:
        print(counter_num)
        counter_num += 1
    else:
        counter_num += 1