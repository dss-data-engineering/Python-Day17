# Here is a turtle race you can bet on.
# Just enter the colour of turtle you pick as the winner and enjoy the race!

from turtle import Turtle, Screen
import random

colours = ["red", "orange", "green", "blue", "purple"]
y_values = [-150, -90, -30, 30, 90]
turtles = []

#initializing screen
screen = Screen()
screen.setup(width=900, height=400)

#initializing the turtles and their starting positions

def create_turtles():
    for turtle_index in range(0,5):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colours[turtle_index])
        new_turtle.penup()
        new_turtle.goto(-200, y_values[turtle_index])
        turtles.append(new_turtle)


def move_forward(turtle_object):
    turtle_object.forward(random.randint(10,20))


def main():
    user_input = screen.textinput("Make Your Bet", "Enter a colour (red, orange, green, blue or purple).").lower()
    while user_input not in ["red", "orange", "green", "blue", "purple"]:
        user_input = screen.textinput("Invalid Choice", "Enter a colour (red, orange, green, blue or purple).")

    create_turtles()

    game_on = True

    while game_on:
        for turtle in turtles:
            if turtle.xcor() > 420:
                game_on = False
                winning_colour = turtle.pencolor()
                result_turtle = Turtle(shape="turtle")
                if user_input == winning_colour:
                    result_turtle.penup()
                    result_turtle.goto(-50, 0)
                    result_turtle.color(winning_colour)
                    result_turtle.write(f"Congratulations! You win! The winner is {turtle.pencolor()}.", align="center", font=("Arial", 24, "bold"))
                    print(f"Congratulations! You win! The winner is {turtle.pencolor()}.")
                else:
                    result_turtle.penup()
                    result_turtle.goto(-50, 0)
                    result_turtle.color(winning_colour)
                    result_turtle.write(f"Sorry. You lose! The winner is {turtle.pencolor()}.", align="center", font=("Arial", 24, "bold"))
                    print(f"Sorry, you lose! The winner is {turtle.pencolor()}.")
            move_forward(turtle)

    screen.listen()
    screen.exitonclick()

main()