import turtle
import pandas as pd
from matplotlib.pyplot import title

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"C:\Users\Khasan\PycharmProjects\PythonProjects\U.S States Game\blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# Load the data
data = pd.read_csv(r"C:\Users\Khasan\PycharmProjects\PythonProjects\U.S States Game\50_states.csv")
all_states = data.state.to_list()
print(all_states)

# Track correct guesses
guessed_states = []

# Game loop
while len(guessed_states) < 50:
    # Prompt for a state name
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States correct",
        prompt="What's another state's name?"
    ).title() # Convert to Title Case

    # Exit the game if the user types "Exit"
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break



    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state) # Add to guessed states


            # The state name on the map
        state_data = data[data.state == answer_state]
        x, y = int(state_data.x), int(state_data.y)

        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        marker.goto(x,y)
        marker.write(answer_state)


screen.exitonclick()