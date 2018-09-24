multiply = 1
while multiply < 11:
    times_what = 1
    while times_what < 11:
        total_value = multiply * times_what
        print('%d X %d = %d' % (multiply, times_what, total_value))
        times_what += 1
    multiply += 1