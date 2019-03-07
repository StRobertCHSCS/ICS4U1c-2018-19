"""
Animation demo of a bouncing ball demonstrating class methods and encapsulation

"""

import arcade

# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bouncing Rectangle Example"

# Size of the rectangle
RECT_WIDTH = 50
RECT_HEIGHT = 50


class Ball(object):

    def __init__(self, start_x, start_y, spd, rad, arcade_colour):
        '''

        :param start_x: the starting x location
        :param start_y: the starting y location
        :param spd: speed of the ball
        :param rad: radius
        :param arcade_colour: colour of the ball
        '''

        self.x = start_x
        self.y = start_y
        self.speed = spd
        self.direction_x = 1
        self.direction_y = 1
        self.radius = rad
        self.colour = arcade_colour

    def move(self):

        # advance the position
        self.x += self.speed * self.direction_x
        self.y += self.speed * self.direction_y

        # Figure out if we hit the edge and need to reverse.
        if self.x < self.radius or self.x > SCREEN_WIDTH - self.radius:
            self.direction_x *= -1

        if self.y < self.radius or self.y > SCREEN_HEIGHT - self.radius:
            self.direction_y *= -1

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.colour)





def on_draw(delta_time):
    """
    Use this function to draw everything to the screen.
    """
    global ball

    # Start the render. This must happen before any drawing
    # commands. We do NOT need a stop render command.
    arcade.start_render()

    ball.draw()
    ball.move()


ball = Ball(SCREEN_WIDTH//4,SCREEN_HEIGHT//3,5,50,arcade.color.PURPLE_HEART)


def main():
    # Open up our window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.WHITE)

    # Tell the computer to call the draw command at the specified interval.
    arcade.schedule(on_draw, 1 / 60)

    # Run the program
    arcade.run()


if __name__ == "__main__":
    main()