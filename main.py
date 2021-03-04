from turtle import Turtle, Screen
import random


def giving_turtles_names():
    all_turtles = []
    y_pos = -120
    for color in colours:
        y_pos += 40
        one_of_the_turtle = Turtle(shape='turtle')
        one_of_the_turtle.fillcolor(color)
        one_of_the_turtle.penup()
        one_of_the_turtle.goto(x=-230, y=y_pos)
        one_of_the_turtle.speed(7)
        all_turtles.append(one_of_the_turtle)
    return all_turtles


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='WHO WINS?', prompt='Type a colour: ').lower()
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtles = giving_turtles_names()

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.fillcolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle first!")
            else:
                print(f"You've lost! The {winning_turtle} turtle first!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()