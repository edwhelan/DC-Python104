height_of_pyramid = int(input('What is the height of your Pyramid? '))
counter = 1
counter_tracker = 1
while counter_tracker <= height_of_pyramid :
    print(height_of_pyramid*" "+ counter * '*')
    height_of_pyramid = height_of_pyramid - 1
    counter = counter + 2
counter_tracker += 1
