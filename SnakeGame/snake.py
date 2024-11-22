import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        """Initialize the snake's body"""
        self.segments = [] # List to hold the segments of the snake
        self.create_snake()  # Create the initial snake body
        self.head = self.segments[0]

    def create_snake(self):
        """Create the initial segments of the snake"""
        for position in STARTING_POSITIONS:
            new_segment = turtle.Turtle("square") # Each segment is a square
            new_segment.color("white") # Set color to white
            new_segment.penup()  # Prevent drawing lines
            new_segment.goto(position)  # Move to the initial position
            self.segments.append(new_segment)  # Add the segment to the segments list

    def move(self):
        """Move the snake forward"""
        # Move each segment to the position of the segment in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1): # Start from the end to avoid overwriting positions
            new_x = self.segments[seg_num - 1].xcor() # Get the x-coordinate of the segment in front
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the segment in front
            self.segments[seg_num].goto(new_x, new_y) # Move current segment to the new position
            # Move the first segment forward
        self.head.forward(MOVE_DISTANCE) # Move the head of the snake forward

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


