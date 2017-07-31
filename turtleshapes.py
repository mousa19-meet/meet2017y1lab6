import turtle
turtle.setup(800,800)
turtle.shape('turtle')
square = turtle.clone()
square.shape('square')
square.goto(100,100)

square.goto(300,300)
square.stamp()
square.goto(100,100)

triangle = turtle.clone()
triangle.shape('triangle')
triangle.goto(-300,-300)
triangle.stamp()
triangle.goto(-200,200)
