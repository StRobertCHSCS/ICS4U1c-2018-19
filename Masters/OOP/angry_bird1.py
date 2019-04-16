
import math

wall_health = 3
wall_x_pos = 20
wall_height = 6
time_interval = 0.1

while wall_health >0:
    theta_degrees = float(input("Enter launch angle: "))
    bird_velocity = float(input("Enter launch velocity (m/s): "))
    bird_xpos = 0 # starting x position of bird
    bird_ypos = 3 # starting y position (height) of bird

    theta = math.radians(theta_degrees)
    bird_xvel = bird_velocity * math.cos(theta)
    bird_yvel = bird_velocity * math.sin(theta)

    hit_ground = False
    hit_wall = False

    while not hit_ground and not hit_wall:
        # calculate the position and velocity in 0.1 seconds
        bird_xpos = bird_xpos + time_interval * bird_xvel
        bird_yvel1 = bird_yvel - time_interval * 9.8
        bird_ypos = bird_ypos + time_interval * (bird_yvel + bird_yvel1)/2.0
        bird_yvel = bird_yvel1

        print("x pos: ", bird_xpos)
        print("y pos: ", bird_ypos)
        print("")

        # check if bird has hit the ground or hit the wall based on xpos, ypos
        if bird_ypos < 0 and bird_xpos < wall_x_pos:
            print("hit ground")
            hit_ground = True

        elif bird_ypos < wall_height and bird_xpos > wall_x_pos:
            hit_wall = True
            wall_health -= 1
            print("hit wall")
            print("wall health:", wall_health)

        print("")

print("wall destroyed, attack the pigs!!!")




