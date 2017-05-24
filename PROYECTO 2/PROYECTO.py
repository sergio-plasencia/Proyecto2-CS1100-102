import turtle
var_13=int(input("Ingrese un número de grados muy loco y entero:"))


turtle.speed(20)

def circulo(n):

    turtle.speed(1000)
    for i in range(n):
        for b in range(15):
            turtle.fd(i)
            turtle.right(6)

def rectangulo(b):
    turtle.pu()
    turtle.home()
    turtle.pd()

    for i in range(1,100):
        turtle.speed(20)
        turtle.color("green")
        turtle.fd(b)
        turtle.right(90)
        turtle.fd(b)
        turtle.right(90)
        turtle.fd(b)
        turtle.right(90)
        turtle.fd(b)
        turtle.right(i)



def triangulo(r):
    for i in range(1,100):
        turtle.color("blue")
        turtle.left(120)
        turtle.fd(r)
        turtle.right(120)
        turtle.fd(r)
        turtle.right(120)
        turtle.fd(r)
        turtle.color("red")
        turtle.right(i)

def circulo3(d):
    turtle.color("red")
    turtle.pensize(1)
    for i in range(28):
        turtle.circle(d*i)
        turtle.circle(-d*i)
        turtle.left(i)

def triangulo2(z):
    turtle.color("orange")
    turtle.home()
    for i in range(50):
        f=100
        turtle.fd(f)
        turtle.left(120)
        turtle.fd(f)
        turtle.left(120)
        turtle.fd(f)
        turtle.left(z)

    # turtle.pu()
    # turtle.goto(280,-120)
    # turtle.pd()
# n>4 ; n es impar :
# n : numero de lados :
# o : angulo del poligono regular :

# def estrella_impar(l,n):
#     turtle.color("red")
#     o = 180*(n-2)/n
#     for i in range (n) :
#         turtle.fd(l)
#         turtle.right(360-(2*o))


def comida(c_2):
    turtle.color("orange")
    turtle.pu()
    turtle.home()
    turtle.fd(150+105)
    turtle.left(90)
    turtle.fd(110)
    turtle.pd()
    for i in range(c_2):
        turtle.left(45)
        turtle.fd(212)
        turtle.left(45)
        turtle.fd(212)
        turtle.left(45)
        turtle.fd(212)
        turtle.left(45)
        turtle.fd(212)
        turtle.left(1)

def poligono_regular(l, n):
    turtle.color("brown")
    #angulo del poligono :
    o=180*(n-2)/n
    for i in range (n) :
        turtle.fd(l)
        turtle.left(180-o)
        turtle.left(i)

def funcion_1():
    turtle.color("black")
    turtle.pu()
    turtle.home()
    turtle.pd()
    turtle.speed(400)
    for i in range (20) :
        turtle.fd(80)
        turtle.right(150)
    turtle.pu()
    turtle.goto(0,-200)
    turtle.pd()

def corazon(l):
    turtle.color("red")
    turtle.pu()
    turtle.home()
    turtle.goto(0,-300)
    turtle.pd()
    turtle.left(45)
    turtle.fd(2*l)
    turtle.left(90)
    turtle.fd(l)
    turtle.left(90)
    turtle.fd(l)
    turtle.right(90)
    turtle.fd(l)
    turtle.left(90)
    turtle.fd(l)
    turtle.left(90)
    turtle.fd(2*l)

# def trianguloinvertido(l):
#     turtle.pu()
#     turtle.home()
#     turtle.left(90)
#     turtle.fd(l/2)
#     turtle.right(90)
#     turtle.fd(l/2)
#     turtle.left(180)
#     turtle.pd()
#     turtle.pensize(5)
#     turtle.fd(l)
#     turtle.left(110)
#     turtle.fd(l*2)
#     turtle.pu()
#     turtle.home()
#     turtle.left(90)
#     turtle.fd(l/2)
#     turtle.right(90)
#     turtle.fd(l/2)
#     turtle.pd()
#     turtle.right(110)
#     turtle.fd(l*2)

def square(lado):
    turtle.pensize(2)
    turtle.home()
    turtle.color("black")
    turtle.pu()
    turtle.fd(lado)
    turtle.pd()

    turtle.left(90)
    turtle.fd(lado)
    turtle.left(90)
    turtle.fd(lado*2)
    turtle.left(90)
    turtle.fd(lado*2)
    turtle.left(90)
    turtle.fd(lado*2)
    turtle.left(90)
    turtle.fd(lado)

def circulo3(var_3):
    turtle.pensize(1)
    turtle.color("blue")
    for i in range(1,10):
        turtle.circle(var_3)
        var_3=var_3-i


def coldplay(var_4):
    turtle.pu()
    turtle.goto(500,0)
    turtle.pd()
    for i in range(1,100):
        turtle.circle(var_4)
        turtle.right(90)
        turtle.pu()
        turtle.fd(var_4)
        turtle.pd()
        turtle.circle(var_4-i)
    turtle.pu()
    turtle.home()
    turtle.pd()
    turtle.color("red")
turtle.color("red")


def metallica(var_5):
    for i in range(50):
        turtle.fd(var_5)
        turtle.left(120)
        turtle.fd(var_5)
        turtle.left(120)
        turtle.fd(var_5)
        turtle.left(i)

def a7x(var_6):
    turtle.pu()
    turtle.home()
    turtle.goto(-300,0)
    turtle.pd()
    turtle.color("black")
    turtle.left(180)
    turtle.fd(300)
    turtle.goto(-300,0)
    turtle.goto(-300,150)
    for i in range (var_6):
        if var_6>50:
            turtle.circle(-var_6)
            var_6=var_6-1
        else:
            turtle.circle(var_6)
            var_6=var_6-1
    turtle.goto(-600,0)
    turtle.goto(-300,-150)

def rueda (l):
    turtle.pu()
    turtle.goto(250,-250)
    turtle.pd()
    turtle.speed(400)
    for i in range (250) :
        turtle.fd(l)
        turtle.right(91)


def trangulo(var_7,var_8):
    turtle.color("yellow")
    turtle.pu()
    turtle.home()
    turtle.goto(-10,-10)
    turtle.pd()
    turtle.speed(400)
    for i in range (20) :
        turtle.fd(var_7)
        turtle.left(110)
        turtle.fd(var_7)
        turtle.left(110)
        turtle.fd(var_7)
        turtle.left(var_8+1)
        var_7=var_7+1
        var_8=var_8+1
        turtle.fd(var_7)
        turtle.left(110)

def corazon(l):
    turtle.pu()
    turtle.home()
    turtle.goto(300,300)
    turtle.pd()
    turtle.right(90)
    turtle.color("red")
    turtle.left(45)
    turtle.fd(2*l)
    turtle.left(90)
    turtle.fd(l)
    turtle.left(90)
    turtle.fd(l)
    turtle.right(90)
    turtle.fd(l)
    turtle.left(90)
    turtle.fd(l)
    turtle.left(90)
    turtle.fd(2*l)

def fibo(var_10,var_11):
    # turtle.pu()
    # turtle.home()
    # turtle.pd()
    turtle.color("green")
    for i in range(var_10):
        var_11=var_11+1
        var_12=var_11+1
        turtle.fd((var_11)+(var_12))
        turtle.left(var_13)

y=int(input("Ingrese grados numero 2: "))
turtle.speed(0)

def fibo2(var_13,var_14):
    turtle.color("red")
    turtle.pu()
    turtle.home()
    turtle.goto(-50,-20)
    turtle.pd()
    for i in range(var_13):
        var_13=var_13+1
        var_14=var_14+1
        for i in range(4):
            turtle.fd((var_13)+(var_14))
            turtle.left(y)



































# def square(lado,n):
#     turtle.home
#     turtle.color("black")
#     turtle.pu()
#     turtle.goto(0,300)
#     turtle.pd()
#     turtle.left(90)
#
#     if n == 0:
#         turtle.forward(lado)
#     else:
#         lado = lado / 3
#         square(lado, n-1)
#         turtle.left(60)
#         square(lado, n-1)
#         turtle.right(120)
#         square(lado, n-1)
#         turtle.left(60)
#         square(lado, n-1)




circulo(26)
rectangulo(50)
triangulo(50)
circulo3(34)
triangulo2(23)

# estrella_impar(500,13)
comida(100)
square(300)
circulo3(300)
coldplay(100)
metallica(200)
a7x(100)
rueda(500)
trangulo(20,110)
corazon(50)
fibo(1000,20)
fibo2(70,50)

poligono_regular(60, 8 )
funcion_1()
corazon(150)
# trianguloinvertido(500)


#  square(1000,5)
turtle.done()
