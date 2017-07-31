import turtle
UP_ARROW ="Up"
LEFT_ARROW = 'Left'
RIGHT_ARROW = 'Right'
DOWN_ARROW = 'Down'
SPACEBAR = "space"

up = 0 
left = 1
down = 2 
right = 3
direction = up

def up_1():
    global direction
    direction = up
    print('up_arrow')
    old_pos = turtle.pos()
    x = old_pos[0]
    y = old_pos[1]
    turtle.goto(x,y+10)
    print(turtle.pos())
def down_1():
    global direction
    direction = down
    print('down_arrow')
    old_pos_2 = turtle.pos()
    x = old_pos_2[0]
    y = old_pos_2[1]
    turtle.goto(x,y-10)
    print(turtle.pos())
def right_1():
    global direction
    direction = right
    print('right_arrow')
    old_pos_3 = turtle.pos()
    x = old_pos_3[0]
    y = old_pos_3[1]
    turtle.goto(x+10,y)
    print(turtle.pos())
def left_1():
    global direction
    direction = left
    print('left_arrow')
    old_pos_4 = turtle.pos()
    x = old_pos_4[0]
    y = old_pos_4[1]
    turtle.goto(x-10,y)
    print(turtle.pos())
#def stampthis():
#    turtle.stamp()
    
turtle.onkeypress(turtle.stamp,SPACEBAR)
turtle.onkeypress(up_1,UP_ARROW)
turtle.onkeypress(down_1,DOWN_ARROW)
turtle.onkeypress(right_1,RIGHT_ARROW)
turtle.onkeypress(left_1,LEFT_ARROW)
turtle.listen()
