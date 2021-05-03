import turtle as turt

timmyt = turt.Turtle()
screen = turt.Screen()


def forwardfunc():
    timmyt.fd(10)

def backwardfunc():
    timmyt.back(10)

def anticlockfunc():
    timmyt.left(10)

def clockfunc():
    timmyt.right(10)

def clearsketch():
    screen.resetscreen()
    timmyt.home()

screen.listen()
screen.onkey(key="w", fun=forwardfunc)
screen.onkey(key="s", fun=backwardfunc)
screen.onkey(key="c", fun=clearsketch)
screen.onkey(key="a", fun=anticlockfunc)
screen.onkey(key="d", fun=clockfunc)


screen.exitonclick()
