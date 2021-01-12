from turtle import Turtle, Screen
from random import randint

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
is_race_on = False

screen = Screen()
screen.setup(width=600, height=600)
player_num = screen.numinput(title='number of player', prompt='choose number between 1 and 6 :')
player_bet = []
for i in range(int(player_num)):
    users_bets = screen.textinput(title='Make your bet', prompt='Which turtle will win this race : ')
    player_bet.append(users_bets)

x = -290

red = Turtle(shape='turtle')
red.color(colors[0])
red.penup()
red.goto(x, 100)

orange = Turtle(shape='turtle')
orange.color(colors[1])
orange.penup()
orange.goto(x, 50)

yellow = Turtle(shape='turtle')
yellow.color(colors[2])
yellow.penup()
yellow.goto(x, 0)

green = Turtle(shape='turtle')
green.color(colors[3])
green.penup()
green.goto(x, -50)

blue = Turtle(shape='turtle')
blue.color(colors[4])
blue.penup()
blue.goto(x, -100)

purple = Turtle(shape='turtle')
purple.color(colors[5])
purple.penup()
purple.goto(x, -150)

all_turtles = [red, orange, yellow, green, blue, purple]
if len(player_bet) > 0:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 290:

            if len(player_bet) == 1:
                if player_bet[0] == turtle.pencolor():
                    print(f"You've won! The {turtle.pencolor()}  turtle is the winner !")
                else:
                    print(f"You've lost! The {turtle.pencolor()}  turtle is the winner !")

            else:

                for i in range(len(player_bet)):

                    if player_bet[i] == turtle.pencolor():
                        print(f"Player {i + 1} won! The {turtle.pencolor()}  turtle is the winner !")
                    else:
                        print(f"Player {i + 1} lost! The {turtle.pencolor()} is turtle the winner !")
            is_race_on = False

screen.exitonclick()
