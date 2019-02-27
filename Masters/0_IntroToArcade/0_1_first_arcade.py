
# ?
import arcade
import os

# ?
arcade.open_window(600, 600, "My First Arcade Program")

# ?
arcade.set_background_color(arcade.color.WHITE)

# ?
arcade.start_render()

# ?
arcade.draw_text("draw_circle_filled", 363, 207, arcade.color.BLACK, 10)
arcade.draw_circle_filled(420, 285, 18, arcade.color.GREEN)

# ?
arcade.finish_render()

# ?
arcade.run()
