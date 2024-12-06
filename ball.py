import turtle

'''def draw_ball(color, size, x, y):
    # draw a circle of radius equals to size at x, y coordinates and paint it with color
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y-size)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()'''

'''def move_ball(i, xpos, ypos, vx, vy, dt):
    # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
    xpos[i] += vx[i]*dt
    ypos[i] += vy[i]*dt'''


'''def update_ball_velocity(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius):
    # if the ball hits the side walls, reverse the vx velocity
    if abs(xpos[i]) > (canvas_width - ball_radius):
        vx[i] = -vx[i]

    # if the ball hits the ceiling or the floor, reverse the vy velocity
    if abs(ypos[i]) > (canvas_height - ball_radius):
        vy[i] = -vy[i]'''


class Ball:
    def __init__(self, color, size, x, y, i, xpos, ypos,
                 vx, vy, dt, canvas_width, canvas_height, ball_radius):
        self.color = color
        self.size = size
        self.x = x
        self.y = y

        self.i = i
        self.xpos = xpos
        self.ypos = ypos
        self.vx = vx
        self.vy = vy
        self.dt = dt

        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius

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

    def draw_ball(self):
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y - self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_ball(self):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.xpos[self.i] += self.vx[self.i] * self.dt
        self.ypos[self.i] += self.vy[self.i] * self.dt

    def update_ball_velocity(self):
        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos[self.i]) > (self.canvas_width - self.ball_radius):
            self.vx[self.i] = -self.vx[self.i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos[self.i]) > (self.canvas_height - self.ball_radius):
            self.vy[self.i] = -self.vy[self.i]

