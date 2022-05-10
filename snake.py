from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Creacion de lista de paleta de colores disponibles
colors=['green','blue','yellow','orange','purple']
#Numero aleatorio entre el 0 y el 4
random_number = randrange(0,5)
#Creacion del color del snake
random_color_snake=colors[random_number]
#Se quita el color del sanke en la lista para que no afecte a la comida
colors.remove(colors[random_number])
#Creacion del color de la comida
random_color_food = colors[random_number]


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    

    for body in snake:
        square(body.x, body.y, 9, random_color_snake)

    square(food.x, food.y, 9, random_color_food)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()