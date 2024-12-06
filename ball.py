import turtle

def draw_ball(color, size, x, y):
    # draw a circle of radius equals to size at x, y coordinates and paint it with color
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y-size)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

def move_ball(i, xpos, ypos, vx, vy, dt):
    # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
    xpos[i] += vx[i]*dt
    ypos[i] += vy[i]*dt


def update_ball_velocity(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius):
    # if the ball hits the side walls, reverse the vx velocity
    if abs(xpos[i]) > (canvas_width - ball_radius):
        vx[i] = -vx[i]

    # if the ball hits the ceiling or the floor, reverse the vy velocity
    if abs(ypos[i]) > (canvas_height - ball_radius):
        vy[i] = -vy[i]


class Ball:
    def __init__(self, color, size, x, y):
        self.color = color
        self.size = size
        self.x = x
        self.y = y

    @property
    def color(self):
        return self.color

    @color.setter
    def color(self, color):
        self.color = color

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, size):
        self.size = size


    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, x):
        self.x = x

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, y):
        self.y = y

