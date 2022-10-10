from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=1200, height=600)
user_bet = screen.textinput(title="Who will win?", prompt="Lewis in black, Max in orange, Fernando in blue, "
                                                          "Mika in grey, Michael in red or Sebastien in navy."
                                                          "\nType in name of the driver who you think will win: ")
names = ["lewis", "max", "fernando", "mika", "michael", "sebastien"]
colors = ["black", "DarkOrange", "LightSkyBlue", "gray80", "red", "navy"]
cars = ["assets/formula_black.gif", "assets/formula_orange.gif", "assets/formula_blue.gif",
        "assets/formula_gray.gif", "assets/formula_red.gif", "assets/formula_navy.gif "]
y_position = [-225, -135, -45, 45, 135, 225]
all_turtles = []

for turtle_index in range(0, 6):
    screen.register_shape(cars[turtle_index])
    names[turtle_index] = Turtle(cars[turtle_index])
    names[turtle_index].color(colors[turtle_index])
    names[turtle_index].penup()
    names[turtle_index].goto(x=-550, y=y_position[turtle_index])
    all_turtles.append(names[turtle_index])

turtle_b = Turtle()
turtle_b.hideturtle()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 530:
            index = colors.index(turtle.pencolor())
            winner = colors[index]
            if winner == "black":
                winner = "lewis"
            if winner == "DarkOrange":
                winner = "max"
            if winner == "LightSkyBlue":
                winner = "fernando"
            if winner == "gray80":
                winner = "mika"
            if winner == "red":
                winner = "michael"
            if winner == "navy":
                winner = "sebastien"

            if winner == user_bet.lower():
                turtle_b.write(f"You have won! {winner.capitalize()} is the winner.",
                               font=('Courier', 30, 'normal'), align='center')
                turtle_b.hideturtle()
            else:
                turtle_b.write(f"Bad luck. {winner.capitalize()} is the winner.",
                               font=('Courier', 30, 'normal'), align='center')
                turtle_b.hideturtle()

            is_race_on = False

screen.exitonclick()
