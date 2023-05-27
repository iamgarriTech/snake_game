from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_position = [{0,0}, (-20, 0), (-40, 0)]

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)

segment_1 = Turtle("square")
segment_1.color("white")

segment_2 = Turtle("square")
segment_2.color("white")
segment_2.goto(-20, 0)

segment_2 = Turtle("square")
segment_2.color("white")
segment_2.goto(-40, 0)











screen.exitonclick()