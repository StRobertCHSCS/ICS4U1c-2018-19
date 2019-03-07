import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# list containing snowflakes
snow_list = []


class Snowflake():
    def __init__(self):
        self.x = 0
        self.y = 0


def draw_snowflake(snowflake):
    arcade.draw_circle_filled(snowflake.x, snowflake.y, 2, arcade.color.WHITE)


def on_draw(delta_time):
    global snow_list
    arcade.start_render()

    for snow in snow_list:
        draw_snowflake(snow)
        snow.y -= 3

        # if it hits the ground, start again at the top
        if snow.y < 0:
            snow.y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT*2)

    arcade.finish_render()


def main():
    global snow_list

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing a Starfield")
    arcade.set_background_color(arcade.color.BLACK)

    # generate snowflakes at random positions above the screen height
    for i in range(150):
        new_snow = Snowflake()
        new_snow.x = random.randint(0, SCREEN_WIDTH)
        new_snow.y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT*2)

        snow_list.append(new_snow)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()


# Call the main function to get the program started.
main()