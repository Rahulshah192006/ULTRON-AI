import turtle

def Amongus():
    BODY_COLOR='red'
    GLASS_COLOR='skyblue'
    b=turtle.getscreen()
    a=turtle.Turtle()
    a.pensize(20)
    a.fillcolor(BODY_COLOR)
    a.begin_fill()
    a.right(90)
    a.forward(50)
    a.right(180)
    a.circle(40,-180)
    a.right(180)
    a.forward(200)
    a.right(180)
    a.circle(100,-180)
    a.backward(20)
    a.left(15)
    a.circle(500,-20)
    a.circle(40,-180)
    a.left(7)
    a.backward(50)
    a.up()
    a.left(90)
    a.forward(10)
    a.right(90)
    a.down()
    a.right(240)
    a.circle(50,-70)
    a.end_fill()
    a.up()
    a.right(230)
    a.forward(100)
    a.left(90)
    a.forward(20)
    a.right(90)
    a.down()
    a.fillcolor(GLASS_COLOR)
    a.begin_fill()
    a.right(150)
    a.circle(90,-55)
    a.right(180)
    a.forward(1)
    a.right(180)
    a.circle(10,-65)
    a.right(180)
    a.forward(110)
    a.right(180)
    a.circle(50,-190)
    a.right(170)
    a.forward(80)
    a.right(180)
    a.circle(45,-30)
    a.end_fill()
    a.up()
    a.right(60)
    a.forward(100)
    a.right(90)
    a.forward(75)
    a.fillcolor(BODY_COLOR)
    a.begin_fill()
    a.down()
    a.forward(30)
    a.right(255)
    a.circle(300,-30)
    a.right(260)
    a.forward(30)
    a.end_fill()
    turtle.done()