#find box width and height
box_width = int(input('Width? '))
box_height = int(input('Height? '))
box_rows = 0
while box_rows < box_height:
    box_cols = 0
    if box_rows == 0 or box_rows == (box_height-1):
        box_cols = 0
        while box_cols < box_width:
            print('*', end='')
            box_cols += 1
        print()
        box_rows += 1
    
   
    # if box_rows == 1 or box_rows < box_height:
    else:
        box_cols = 0
        while box_cols < box_width:
            if box_cols == 0 or box_cols == (box_width -1) :
                print('*', end='')
                box_cols += 1
            else:
                print(' ', end='')    
                box_cols += 1
        print()
        box_rows += 1
   
    
