import turtle
import random


class Ball:
    def __init__(self, canvas_width, canvas_height, ball_radius):
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius
        self.num_balls = 0

    def draw_circle(self,color, x, y, size):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()

    def move_circle(self, i):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.xpos[i] += self.vx[i]
        self.ypos[i] += self.vy[i]

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos[i] + self.vx[i]) > (self.canvas_width - self.ball_radius):
            self.vx[i] = -self.vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos[i] + self.vy[i]) > (self.canvas_height - self.ball_radius):
            self.vy[i] = -self.vy[i]

    def set_num(self, num_balls):
        self.num_balls = num_balls

    def get_num(self):
        return self.num_balls

    def initializing(self):
        # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
        for i in range(self.num_balls):
            self.xpos.append(random.randint(-1 * self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius))
            self.ypos.append(random.randint(-1 * self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius))
            self.vx.append(random.randint(1, 0.01 * self.canvas_width))
            self.vy.append(random.randint(1, 0.01 * self.canvas_height))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def show(self):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        while True:
            turtle.clear()
            for i in range(self.num_balls):
                self.draw_circle(self.ball_color[i], self.xpos[i], self.ypos[i], self.ball_radius)
                self.move_circle(i)
            turtle.update()


num_balls = int(input("Number of balls to simulate: "))
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
ball = Ball(canvas_width, canvas_height, ball_radius)
ball.set_num(num_balls)
ball.initializing()
ball.show()
