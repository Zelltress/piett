#Case-study #1
#Developers: Cherkashina D., Ivanova A., Gulakova Y.

import turtle

turtle.setup(1980, 1080) #set the size of the window where the turtle draws
turtle.speed(10)

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

def rhomb(x, y, a):

    '''
    Function, drawing rhomb
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a rhomb
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(30)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(60)
    turtle.left(30)

def rhomb_for_dog(x, y, a):
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

def triangle_rv(x, y, a, b):

    '''
    Function, drawing equilateral triangle
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: size of equal sides
    :param b: the size of the third side
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(125)
    turtle.forward(a)
    turtle.right(145)
    turtle.forward(b)
    turtle.right(145)
    turtle.forward(a)
    turtle.left(55)

def triangle_pr_1(x, y, a, b):

    '''
    Function, drawing rectangular triangle
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: the size of the cathets
    :param b: the size of the hypotenuse
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(45)

def triangle_pr_2(x, y, a, b):

    '''
     Function, drawing rectangular triangle
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(135)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)

def triangle_rvs_1(x, y, a):

    '''
    Function, drawing equilateral triangle
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: the size of the triangle side
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

def triangle_pr_4(x, y, a, b, c): #tr4
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

def triangle_pr_3(x, y, a, b): #tr2
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

def circle(x, y, a):
    turtle.color('black')
    turtle.fillcolor('LightBlue')
    turtle.begin_fill()
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.circle(a)
    turtle.end_fill()

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

def rectangle_for_table(x, y, a, b):

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

def paint_dog():
    turtle.fillcolor('DarkGoldenrod2')
    turtle.begin_fill()
    rhomb_for_dog(425, 287, 30)
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
    triangle_pr_4(295, 333, 50, 90, 79)
    turtle.end_fill()

    turtle.fillcolor('orange')
    turtle.begin_fill()
    rhomb_for_dog(295, 333, 24)
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
    rhomb_for_dog(420, 25, 35)
    turtle.end_fill()

    turtle.fillcolor('darkslateblue')
    turtle.begin_fill()
    triangle_pr_3(350, -40, 100, 141)
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
The man is probably a representative of a mafia group
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
    rhomb_for_men(0, 210, 20)
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
Creating a computer desk with decorative elements
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
    rectangle_for_table(-100, -220, 200, 20)
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

def main ():

#draw rabbit
    turtle.fillcolor('SteelBlue')
    turtle.begin_fill()
    triangle_pr_1(-700, 390, 100, 142)
    turtle.end_fill()

    turtle.fillcolor('PaleTurquoise')
    turtle.begin_fill()
    triangle_pr_2(-700, 287, 100, 143)
    turtle.end_fill()

    turtle.fillcolor('LightSteelBlue')
    turtle.begin_fill()
    triangle_rv(-668, 300, 50, 82)
    turtle.end_fill()

    turtle.fillcolor('LightSkyBlue')#
    turtle.begin_fill()
    triangle_rvs_2(-770, 228, 50)
    turtle.end_fill()

    turtle.fillcolor('CornflowerBlue')
    turtle.begin_fill()
    square(-834, 300, 30)
    turtle.end_fill()

    turtle.fillcolor('CornflowerBlue')
    turtle.begin_fill()
    square(-700, 430, 45)
    turtle.end_fill()

    turtle.fillcolor('CadetBlue')
    turtle.begin_fill()
    parallelogram(-750, 475, 35, 60, 45, 135)
    turtle.end_fill()

#draw dog
    turtle.fillcolor('PaleTurquoise')
    turtle.begin_fill()
    triangle_pr_2(-700, 100, 100, 142)
    turtle.end_fill()

    turtle.fillcolor('CadetBlue')
    turtle.begin_fill()
    parallelogram(-845, 100, 45, 90, 135, 45)
    turtle.end_fill()

    turtle.fillcolor('SkyBlue')
    turtle.begin_fill()
    rhomb(-520, 140, 75)
    turtle.end_fill()

    turtle.fillcolor('CadetBlue')
    turtle.begin_fill()
    parallelogram(-810, -5, 50, 90, 80, 100)
    turtle.end_fill()

    turtle.fillcolor('CadetBlue')
    turtle.begin_fill()
    parallelogram(-695, 100, 100, 140, 135, 45)
    turtle.end_fill()

    turtle.fillcolor('SteelBlue')
    turtle.begin_fill()
    triangle_pr_1(-590, 100, 100, 142)
    turtle.end_fill()

    turtle.fillcolor('SteelBlue')
    turtle.begin_fill()
    triangle_pr_1(-753, 60, 60, 85)
    turtle.end_fill()

    turtle.fillcolor('CadetBlue')
    turtle.begin_fill()
    parallelogram(-640, 23, 35, 120, 80, 100)
    turtle.end_fill()

    turtle.fillcolor('LightSteelBlue')
    turtle.begin_fill()
    triangle_rv(-600, 35, 50, 82)
    turtle.end_fill()

    turtle.fillcolor('CornflowerBlue')
    turtle.begin_fill()
    square(-545, 160, 63)
    turtle.end_fill()

    turtle.fillcolor('SteelBlue')
    turtle.begin_fill()
    triangle_pr_1(-515, 190, 30, 43)
    turtle.end_fill()

    turtle.fillcolor('CadetBlue')
    turtle.begin_fill()
    parallelogram(-480, 127, 35, 35, 120, 60)
    turtle.end_fill()


#draw shark
    turtle.fillcolor('Teal')
    turtle.begin_fill()
    triangle_rvs_1(-710, -395, 30)
    turtle.end_fill()

    turtle.fillcolor('LightSteelBlue')
    turtle.begin_fill()
    triangle_rv(-570, -410, 60, 98)
    turtle.end_fill()

    turtle.fillcolor('CadetBlue')
    turtle.begin_fill()
    parallelogram(-649, -300, 270, 141, 135, 45)
    turtle.end_fill()

    turtle.fillcolor('LightSteelBlue')
    turtle.begin_fill()
    triangle_rv(-530, -410, 60, 98)
    turtle.end_fill()

    turtle.fillcolor('SteelBlue')
    turtle.begin_fill()
    triangle_pr_1(-758, -300, 100, 142)
    turtle.end_fill()

    turtle.fillcolor('PaleTurquoise')
    turtle.begin_fill()
    triangle_pr_2(-654, -300, 100, 142)
    turtle.end_fill()

    turtle.fillcolor('LightSteelBlue')
    turtle.begin_fill()
    triangle_rv(-860, -400, 75, 123)
    turtle.end_fill()

    turtle.fillcolor('SteelBlue')
    turtle.begin_fill()
    triangle_pr_1(-550, -208, 90, 127)
    turtle.end_fill()

    turtle.fillcolor('CornflowerBlue')
    turtle.begin_fill()
    square(-470, -325, 10)
    turtle.end_fill()

    turtle.fillcolor('CadetBlue')
    turtle.begin_fill()
    parallelogram(-500, -330, 5, 30, 80, 100)
    turtle.end_fill()

    turtle.fillcolor('CadetBlue')
    turtle.begin_fill()
    parallelogram(-515, -330, 5, 30, 80, 100)
    turtle.end_fill()

    turtle.fillcolor('SteelBlue')
    turtle.begin_fill()
    triangle_pr_1(-495, -324, 5, 7)
    turtle.end_fill()

    turtle.fillcolor('SteelBlue')
    turtle.begin_fill()
    triangle_pr_1(-510, -324, 5, 7)
    turtle.end_fill()

    olen()
    men()
    table()

    paint_Gosha()
    paint_home()
    paint_dog()

    turtle.done()

if __name__ == '__main__':
    main()
