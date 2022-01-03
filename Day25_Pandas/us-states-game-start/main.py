import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
state_list = state_data["state"].to_list()
score = 0

answer_state = screen.textinput(title="Guess the State", prompt="What's a state's name?")

while len(state_list) > 0 and answer_state:
	if answer_state.lower() in state_list.lower():
		state_list.pop(state_list.index(answer_state))
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		state = state_data[state_data.state == answer_state]
		t.goto(int(state.x), int(state.y))
		t.write(answer_state)
		score += 1

	answer_state = screen.textinput(title=f"{score} of 50 states", prompt="What's another state's name?")

screen.exitonclick()
