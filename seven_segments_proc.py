import turtle


class Draw_num:

    def __init__(self, color):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)

        self.color = color
        self.penup()
        self.setheading(0)
        self.goto(0, 0)
        self.pensize(10)


    def draw(self, digit):
        if digit == 0:
            self.goto(-50, 100)
            self.pendown()
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.forward(100)
            self.right(90)
            self.penup()

        if digit == 1:
            self.goto(50, 100)
            self.pendown()
            self.right(90)
            self.forward(100)
            self.forward(100)
            self.left(90)
            self.penup()

        if digit == 2:
            self.goto(-50, 100)
            self.pendown()
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.left(90)
            self.forward(100)
            self.left(90)
            self.forward(100)
            self.penup()

        if digit == 3:
            self.goto(-50, 100)
            self.pendown()
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.forward(-100)
            self.left(90)
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.left(90)
            self.left(90)
            self.penup()

        if digit == 4:
            self.goto(-50, 100)
            self.pendown()
            self.right(90)
            self.forward(100)
            self.left(90)
            self.forward(100)
            self.left(90)
            self.forward(100)
            self.forward(-100)
            self.forward(-100)
            self.right(90)
            self.penup()

        if digit == 5:
            self.goto(-50, 100)
            self.pendown()
            self.forward(100)
            self.forward(-100)
            self.right(90)
            self.forward(100)
            self.left(90)
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.left(90)
            self.left(90)
            self.penup()

        if digit == 6:
            self.draw(5)
            self.goto(-50, 0)
            self.pendown()
            self.right(90)
            self.forward(100)
            self.left(90)
            self.penup()
        
        if digit == 7:
            self.goto(-50, 100)
            self.pendown()
            self.forward(100)
            self.forward(-100)
            self.draw(1)

        if digit == 8:
            self.draw(0)
            self.goto(-50, 0)
            self.pendown()
            self.forward(100)
            self.penup()

        if digit == 9:
            self.draw(5)
            self.goto(50, 100)
            self.pendown()
            self.right(90)
            self.forward(100)
            self.left(90)
            self.penup()

    def clear(self,my_turtle):
        my_turtle.clear()

    def my_delay(self,dt):
        import time
        start =  time.time()
        while time.time() - start < dt:
            pass

Tom = turtle.Turtle()
tom_color = (255, 0, 0)
Draw_num(Tom , tom_color)
delay_in_seconds = 0.2
while True:
    for i in range(0, 10):
        Draw_num.clear(Tom)
        Draw_num.draw(Tom, i)
        Draw_num.my_delay(delay_in_seconds)
        turtle.update()

turtle.done()

