import turtle
turtle.speed(100)
turtle.setup(1000, 800)
def triangle(x, y, a, b):

    '''
    Function, drawing rectangular triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a triangle
    :param b: side length of b triangle
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(b)
    turtle.left(135)

def triangle4(x, y, a, b, c):
    '''
    Function, drawing rectangular triangle.
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param a: side length of a triangle
    :param b: side length of b triangle
    :param c: side length of c triangle
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(60)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(b)    #Hypotenuse.
    turtle.right(147)
    turtle.forward(c)
    turtle.right(33)

def triangle2(x, y, a, b):
    '''
    Function, drawing rectangular triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a triangle
    :param b: side length of b triangle
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.left(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.left(180)

def triangle_pr_5(x, y, a, b):
    '''
    Function, drawing rectangular triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a triangle
    :param b: side length of b triangle
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(90)

def triangle_rvs_1(x, y, a):
    '''
    Function, drawing isosceles triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a triangle
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)

def triangle_rvs_3(x, y, a):
    '''
    Function, drawing isosceles triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a triangle
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(60)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.left(60)

def square(x, y, a):
    '''
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a square
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)

def rectangle(x, y, a, b):
    '''
    Function, drawing rectangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a rectangle
    :param b: side length of b rectangle
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)

def parallelogram (x, y, a, b, c, d):
    '''
    Function, drawing parallelogram.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a parallelogram.
    :param b: side length of b parallelogram.
    :param c: angle value of c parallelogram.
    :param d: angle value of d parallelogram.
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(c)
    turtle.forward(b)
    turtle.right(d)
    turtle.forward(a)
    turtle.right(c)      #Blunt angle.
    turtle.forward(b)
    turtle.right(d)      #Sharp angle.


def rhomb (x, y, a):
    '''
    Function, drawing rhomb.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a rhomb
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(60)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(60)

def circle(x, y, a):
    turtle.color('black')
    turtle.fillcolor('LightBlue')
    turtle.begin_fill()
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.circle(a)
    turtle.end_fill()

def paint_dog():
    turtle.fillcolor('DarkGoldenrod2')
    turtle.begin_fill()
    rhomb(425, 287, 30)
    turtle.end_fill()

    turtle.fillcolor('gold2')
    turtle.begin_fill()
    parallelogram(290,260, 120, 60, 60, 120)
    turtle.end_fill()

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    triangle_rvs_1(410, 208, 30)
    turtle.end_fill()

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    triangle_rvs_1(320, 208, 30)
    turtle.end_fill()

    turtle.fillcolor('plum2')
    turtle.begin_fill()
    square(290, 290, 30)
    turtle.end_fill()

    turtle.fillcolor('lavender')
    turtle.begin_fill()
    triangle4(295, 333, 50, 90, 79)
    turtle.end_fill()

    turtle.fillcolor('orange')
    turtle.begin_fill()
    rhomb(295, 333, 24)
    turtle.end_fill()

    circle(270, 302, 5)

def paint_home():
    turtle.fillcolor('mistyrose')
    turtle.begin_fill()
    square(250, -270, 90)
    turtle.end_fill()

    turtle.fillcolor('orange')
    turtle.begin_fill()
    rectangle(320, -270, 135, 90)
    turtle.end_fill()

    turtle.fillcolor('blue')
    turtle.begin_fill()
    parallelogram(285, -208, 150, 70, 60, 120)
    turtle.end_fill()

    turtle.fillcolor('MediumOrchid1')
    turtle.begin_fill()
    triangle_rvs_3(285, -208, 70)
    turtle.end_fill()

    circle(285, -263, 14)

    turtle.fillcolor('orange')
    turtle.begin_fill()
    rectangle(270, -305, 25, 55)
    turtle.end_fill()

    turtle.fillcolor('lightcyan2')
    turtle.begin_fill()
    square(400, -290, 35)
    turtle.end_fill()

    turtle.fillcolor('lightcyan2')
    turtle.begin_fill()
    square(345, -290, 35)
    turtle.end_fill()

    turtle.fillcolor('orange')
    turtle.begin_fill()
    rectangle(303, -315, 6, 6)
    turtle.end_fill()

    turtle.fillcolor('mediumpurple1')
    turtle.begin_fill()
    rectangle(325, -188, 15, 40)
    turtle.end_fill()

    turtle.fillcolor('pink')
    turtle.begin_fill()
    triangle_pr_5(345, -290, 24, 17)
    turtle.end_fill()

    turtle.fillcolor('pink')
    turtle.begin_fill()
    triangle_pr_5(400, -290, 24, 17)
    turtle.end_fill()

    turtle.color('black')
    turtle.up()
    turtle.setposition(400, -307)
    turtle.down()
    turtle.forward(35)
    turtle.up()
    turtle.setposition(345, -307)
    turtle.down()
    turtle.forward(35)

    turtle.up()
    turtle.setposition(417, -290)
    turtle.right(90)
    turtle.down()
    turtle.forward(35)
    turtle.up()
    turtle.setposition(362, -290)
    turtle.down()
    turtle.forward(35)
    turtle.left(90)

    turtle.up()
    turtle.setposition(285, -235)
    turtle.right(90)
    turtle.down()
    turtle.forward(28)
    turtle.left(90)
    turtle.up()
    turtle.setposition(271, -250)
    turtle.down()
    turtle.forward(28)
    turtle.up()

def paint_Gosha():
    turtle.fillcolor('lightslateblue')
    turtle.begin_fill()  #For backcolor.
    triangle(250, -40, 100, 141)
    turtle.end_fill()  # For backcolor.

    turtle.fillcolor('pink')
    turtle.begin_fill()
    rhomb(420, 25, 35)
    turtle.end_fill()

    turtle.fillcolor('darkslateblue')
    turtle.begin_fill()
    triangle2(350, -40, 100, 141)
    turtle.end_fill()

    circle(300, 13, 10)
    circle(385, 13, 10)

    turtle.fillcolor('plum1')
    turtle.begin_fill()
    rectangle(310, 100, 70, 40)
    turtle.end_fill()

    turtle.fillcolor('plum1')
    turtle.begin_fill()
    triangle_rvs_1(280, -40, 30)
    turtle.end_fill()

    turtle.fillcolor('slateblue')
    turtle.begin_fill()
    triangle_rvs_1(370, -40, 30)
    turtle.end_fill()

    turtle.fillcolor('purple4')
    turtle.begin_fill()
    square(330, 90, 10)
    turtle.end_fill()

    turtle.fillcolor('blue')
    turtle.begin_fill()
    parallelogram(355, 100, 25, 15, 120, 60)
    turtle.end_fill()

    turtle.fillcolor('thistle1')
    turtle.begin_fill()
    rectangle(280, 70, 40, 5)
    turtle.end_fill()


paint_dog()
paint_Gosha()
paint_home()
turtle.done()