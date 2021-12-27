from turtle import Turtle, Screen
from math import ceil
import random

screen_width = 500
screen_height = 400
finish_line_contra = 40
n_turtles = 5

def config_turtle(turtle_obj, instance):
	turtle_obj.penup()
	turtle_obj.goto(x=-(screen_width-20)/2, y=(((screen_height/2)-50)-(((screen_height-50)/n_turtles)*instance)))

	R = random.random()
	B = random.random()
	G = random.random()
	turtle_obj.color(R,B,G)

def check_winner(turtle_dict):
	for key, value in turtle_dict.items():
		if value.xcor() >= (screen_width/2) - finish_line_contra:
			return key

if __name__ == "__main__":
	screen = Screen()
	screen.setup(width=screen_width, height=screen_height)

	user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a number between 1 and {n_turtles}: ")

	if user_bet:
		print(f"You have bet on turtle {user_bet}")
		# draw vertical finish line
		ump_turtle = Turtle()
		ump_turtle.penup()
		ump_turtle.goto(x=((screen_width/2)-finish_line_contra), y=250)
		ump_turtle.right(90)
		for y in range(0,ceil((screen_width/3)*2)):
			if y%10==0: ump_turtle.dot()
			ump_turtle.forward(2)




		turtle_dict = dict()

		for index in range(0, n_turtles):
			turtle_dict[index] = Turtle(shape="turtle")
			config_turtle(turtle_dict[index], index)

		is_race_on = True
		while is_race_on:
			rand_distance = random.randint(0,10)
			rand_turtle = random.randint(0, n_turtles-1)
			turtle_dict[rand_turtle].forward(rand_distance)
			winner = check_winner(turtle_dict)
			if winner is not None: is_race_on = False

		if winner + 1 == user_bet: 
			print(f"Turtle {winner + 1} wins.. meaning you win!")
		else: print(f"Turtle {winner + 1} wins.. meaning you lost..")

		screen.exitonclick()
	else: screen.bye()
