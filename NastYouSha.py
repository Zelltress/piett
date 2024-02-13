import turtle

turtle.setup(1000, 800) #set the size of the window where the turtle draws
turtle.speed(10)

def triangle_rvs_1(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)

def triangle_rvs_2(x, y, a):
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

def triangle_rvs_3(x, y, a):
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


def parallelogram(x, y, a, b, c, d):

    '''
    Function, drawing parallelogram
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a parallelogram
    :param b: side width of a parallelogram
    :param c: a first pair of  corners
    :param d: a second pair of corners
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
    turtle.right(c)
    turtle.forward(b)
    turtle.right(d)
    turtle.end_fill()


def rhomb_for_men(x, y, a):

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(120)

def rectangle(x, y, a, b):

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

def rectangle_2(x, y, a, b):

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

'''
Оленёнок!
'''
def olen():
    turtle.fillcolor('#FDF5E6')
    turtle.begin_fill()
    square(-100, 90, 200)
    turtle.end_fill()

    turtle.right(180)

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    parallelogram(0, 0, 50, 70, 45, 135)
    turtle.end_fill()

    turtle.left(180)

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    parallelogram(49, 49, 50, 70, 135, 45)
    turtle.end_fill()

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    triangle_rvs_1(0, 0, 100)
    turtle.end_fill()

    turtle.fillcolor('#030119')
    turtle.begin_fill()
    triangle_rvs_2(0, 0,75)
    turtle.end_fill()

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    triangle_rvs_3(100, 0,50)
    turtle.end_fill()

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    triangle_rvs_1(-100, 0,100)
    turtle.end_fill()

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    triangle_rvs_3(-100, 0,50)
    turtle.end_fill()

    turtle.fillcolor('#030119')
    turtle.begin_fill()
    triangle_rvs_2(100, 50,58)
    turtle.end_fill()

    turtle.fillcolor('#030119')
    turtle.begin_fill()
    triangle_rvs_2(-100, 50,58)
    turtle.end_fill()

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    triangle_rvs_1(-37, -63,75)
    turtle.end_fill()

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    parallelogram(69, 139, 30, 70, 135, 45)
    turtle.end_fill()

    turtle.right(180)

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    parallelogram(-20, 90, 30, 70, 45, 135)
    turtle.end_fill()

    turtle.right(15)

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    triangle_rvs_3(40, 110, 30)
    turtle.end_fill()

    turtle.left(15)
    turtle.left(15)

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    triangle_rvs_3(-40, 110, 30)
    turtle.end_fill()

    turtle.right(15)
    turtle.left(180)
'''
Мужчина, вероятно, представитель мафиозной группировки
'''

def men():
    turtle.fillcolor('#FDF5E6')
    turtle.begin_fill()
    square(-25, 280, 50)
    turtle.end_fill()

    turtle.fillcolor('#FDF5E6')
    turtle.begin_fill()
    square(-5, 230, 10)
    turtle.end_fill()

    turtle.fillcolor('#000000')
    turtle.begin_fill()
    rectangle(-50, 220, 100, 50)
    turtle.end_fill()

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    triangle_rvs_1(-5, 220, 10)
    turtle.end_fill()

    turtle.right(58)

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    rhomb(0, 210, 20)
    turtle.end_fill()

    turtle.left(58)

    turtle.fillcolor('#000000')
    turtle.begin_fill()
    rectangle(-50, 300, 100, 20)
    turtle.end_fill()

    turtle.fillcolor('#000000')
    turtle.begin_fill()
    rectangle(-27, 370, 55, 70)
    turtle.end_fill()

    turtle.right(180)

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    parallelogram(-5, 270, 5, 15, 45, 135)
    turtle.end_fill()

    turtle.left(180)

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    parallelogram(15, 281, 5, 15, 135, 45)
    turtle.end_fill()

    turtle.fillcolor('#000000')
    turtle.begin_fill()
    square(10, 260, 10)
    turtle.end_fill()

    turtle.fillcolor('#000000')
    turtle.begin_fill()
    square(-20, 260, 10)
    turtle.end_fill()

'''
Создание компьютерного стола с декоротивными элементами 
'''
def table():
    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    parallelogram(0, -240, 50, 70, 45, 135)
    turtle.end_fill()

    turtle.right(180)

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    parallelogram(-50, -289, 50, 70, 135, 45)
    turtle.end_fill()

    turtle.left(180)

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    rectangle_2(-100, -220, 200, 20)
    turtle.end_fill()

    turtle.fillcolor('#000000')
    turtle.begin_fill()
    rectangle(30, -210, 30, 10)
    turtle.end_fill()

    turtle.fillcolor('#000000')
    turtle.begin_fill()
    rectangle(40, -200, 10, 10)
    turtle.end_fill()

    turtle.fillcolor('#000000')
    turtle.begin_fill()
    rectangle(5, -160, 80, 40)
    turtle.end_fill()

    turtle.fillcolor('#000000')
    turtle.begin_fill()
    rectangle(-50, -200, 10, 20)
    turtle.end_fill()

    turtle.fillcolor('#000000')
    turtle.begin_fill()
    rectangle(-48, -192, 5, 8)
    turtle.end_fill()

    turtle.fillcolor('#FDF5E6')
    turtle.begin_fill()
    square(-80, -205, 15)
    turtle.end_fill()

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    triangle_rvs_3(-75, -200, 5)
    turtle.end_fill()

    turtle.fillcolor('#ff8c00')
    turtle.begin_fill()
    triangle_rvs_3(-70, -200, 5)
    turtle.end_fill()


def main():
    '''
    Main function.
    :return: None
    '''

    olen()
    men()
    table()
    turtle.done()

main()
