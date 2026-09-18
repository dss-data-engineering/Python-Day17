# We recreate a version of the classic toy 'Etch-A-Sketch' using the Turtle library
# Take turns pressing keys w, s, a, d and c to draw

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def move_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_drawing():
    tim.reset()

def main():
    screen.onkey(move_forwards, "w")
    screen.onkey(move_backwards, "s")
    screen.onkey(move_counter_clockwise, "a")
    screen.onkey(move_clockwise, "d")
    screen.onkey(clear_drawing, "c")

    screen.listen()
    screen.exitonclick()

main()