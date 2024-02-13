#Case-study #1
#Developers: Cherkashina D., Ivanova A.,  .

import turtle

turtle.setup(1000, 800) #set the size of the window where the turtle draws
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

    '''
    Function, drawing equilateral triangle
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

def main():

    '''
    Main function.
    :return: None
    '''

    #draw rabbit
    triangle_pr_1(-700, 390, 100, 142)
    triangle_pr_2(-700, 287, 100, 143)
    triangle_rv(-668, 300, 50, 82)
    triangle_rvs_2(-770, 228, 50)
    square(-834, 300, 30)
    square(-700, 430, 45)
    parallelogram(-750, 475, 35, 60, 45, 135)

    #draw dog
    triangle_pr_2(-700, 100, 100, 142)
    parallelogram(-845, 100, 45, 90, 135, 45)
    rhomb(-520, 140, 75)
    parallelogram(-810, -5, 50, 90, 80, 100)
    parallelogram(-695, 100, 100, 140, 135, 45)
    triangle_pr_1(-590, 100, 100, 142)
    triangle_pr_1(-753, 60, 60, 85)
    parallelogram(-640, 23, 35, 120, 80, 100)
    triangle_rv(-600, 35, 50, 82)
    square(-545, 160, 63)
    triangle_pr_1(-515, 190, 30, 43)
    parallelogram(-480, 127, 35, 35, 120, 60)

    #draw shark
    triangle_rvs_1(-710, -395, 30)
    triangle_rv(-570, -410, 60, 98)
    parallelogram(-649, -300, 270, 141, 135, 45)
    triangle_rv(-530, -410, 60, 97)
    triangle_pr_1(-758, -300, 100, 142)
    triangle_pr_2(-654, -300, 100, 142)
    triangle_rv(-860, -400, 75, 122)
    triangle_pr_1(-550, -208, 90, 127)
    square(-470, -325, 10)
    parallelogram(-500, -330, 5, 30, 80, 100)
    parallelogram(-515, -330, 5, 30, 80, 100)
    triangle_pr_1(-495, -324, 5, 8)
    triangle_pr_1(-510, -324, 5, 8)

    turtle.done()

if __name__ == '__main__':
    main()


