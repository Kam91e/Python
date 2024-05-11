import turtle
import math

g = float(input('Podaj przyciąganie planety ("." zamiast ","): '))
v0u = int(input("Czy znasz prędkość początkową (1 tak, 0 nie): "))
alphau = int(input("Czy znasz kąt początkowy (1 tak, 0 nie): "))
if v0u == 1 and alphau == 1:
    v0 = float(input('Podaj prędkość początkową ("." zamiast ","): '))
    alpha = math.radians(float(input('Podaj kąt początkowy ("." zamiast ",")(+ do góry, - w dół): ')))
    v0x = math.cos(alpha)*v0
    v0y = math.sin(alpha)*v0
elif alphau == 0 and v0u == 0:
    v0x = float(input('Podaj prędkość początkową poziomą ("." zamiast ","): '))
    v0y = float(input('Podaj prędkość początkową pionową ("." zamiast ","): '))
elif v0u == 1 and alphau == 0:
    v0xu = int(input("Czy znasz prędkość początkową poziomą (1 tak, 0 nie): "))
    v0 = float(input('Podaj prędkość początkową ("." zamiast ","): '))
    if v0xu == 1:
        v0x = float(input('Podaj prędkość początkową poziomą ("." zamiast ","): '))
        v0y = math.sqrt(v0**2+v0x**2)
    else:
        v0y = float(input('Podaj prędkość początkową pionową ("." zamiast ","): '))
        v0x = math.sqrt(v0**2+v0y**2)
elif v0u == 0 and alphau == 1:
    v0xu = int(input("Czy znasz prędkość początkową poziomą (1 tak, 0 nie): "))
    alpha = math.radians(float(input('Podaj kąt początkowy ("." zamiast ",")(+ do góry, - w dół): ')))
    if v0xu == 1:
        v0x = float(input('Podaj prędkość początkową poziomą ("." zamiast ","): '))
        v0y = math.tan(alpha)*v0x
    else:
        v0y = float(input('Podaj prędkość początkową pionową ("." zamiast ","): '))
        v0x = 1/(math.tan(alpha)/v0y)
y0 = float(input('Podaj wysokość początkową wyżutu ("." zamiast ","): '))
x0 = 0


width = 800
height = 600
ldx, ldy = -10, -100
pgx, pgy = width-10, height-100
screen = turtle.Screen()
screen.setup(width,height)
screen.setworldcoordinates(ldx,ldy,pgx,pgy)

ball = turtle.Turtle(shape='circle', visible=False)
ball.turtlesize(stretch_wid=0.75)
radius = ball.turtlesize()[0]*20/2

ball.penup()
ball.radians()
ball.setheading(0)

ball.goto(ldx,0)
ball.color('green')
ball.pendown()
ball.goto(width,0)
ball.penup()
ball.color('red')

ball.goto(x0,y0)
ball.pendown()
ball.showturtle()
ball.stamp()

t = 0
y = y0
while True:
    t = t+0.1
    vy = v0y-g*t
    v = math.sqrt(vy**2+v0x**2)
    x = x0 + v0x*t
    y = y0 + v0y*t - (g*t**2)/2

    if y <= 0:
        break

    ball.goto(x,y)
    ball.stamp()

print(f'Piłka wylądowawała {x:.2f} od miejsca wyżutu w czasie {t}')
