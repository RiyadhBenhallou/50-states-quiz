from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
turtle = Turtle()
screen.title("U.S. States Game")
screen.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')

data = pd.read_csv('50_states.csv')
states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    text_input = screen.textinput(f'{len(guessed_states)}/50 States Guessed', 'Enter state name').title()
    if text_input == 'Exit':
        missing_states = [state for state in states if state not in guessed_states]
        df = pd.DataFrame(missing_states)
        df.to_csv('states_to_learn.csv')
        break
    elif text_input in states and text_input not in guessed_states:
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == text_input]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(text_input)
        guessed_states.append(text_input)


screen.exitonclick()