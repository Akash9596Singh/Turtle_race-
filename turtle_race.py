import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)  # screen set up screen size
color_list = ['yellow', 'red', 'blue', 'orange', 'green', 'purple']
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter a color: ")
y_position = [-100, -66, -32, 2, 36, 70]
all_turtle = []
tim = Turtle()
tim.penup()
tim.hideturtle()
for i in range(6):
    new_turtle = Turtle('turtle')
    new_turtle.color(color_list[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtle.append(new_turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 220:
            is_race_on = False
            if user_bet == turtle.pencolor():
                tim.write(f"{turtle.pencolor()} is the winner.....", move=False, align='center',
                          font=('Arial', 50, 'normal'))
                # print(f"You win!The winner is {turtle.pencolor()}")
            else:

                # print(f"You loose! The winner is {turtle.pencolor()}")
                tim.write(f"You Loose.....", move=False, align='center',
                          font=('Arial', 50, 'normal'))
            break
screen.exitonclick()
