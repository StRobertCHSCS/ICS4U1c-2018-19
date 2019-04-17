import math



class Wall():

    def __init__(self, init_x_pos, init_height):
        self.__x = init_x_pos
        self.__height = init_height
        self.__health = 3

    def get_health(self):
        """
        Return wall health
        :return: int
        """
        return self.__health

    def collide(self, bird_obj):
        """
        check if a bird has collided with the wall, if so decrease health
        :param bird_obj: an instance of a Bird class
        :return: Boolean
        """
        if bird_obj.get_y() < self.__height and bird_obj.get_x() > self.__x:
            self.__health -= 1
            return True
        else:
            return False

    def is_destroyed(self):
        return self.__health == 0



class Bird():

    def __init__(self, init_theta, init_vel):

        self.__x = 0
        self.__y = 3

        self.__theta = math.radians(init_theta)

        self.__xvel = init_vel * math.cos(self.__theta)
        self.__yvel = init_vel * math.sin(self.__theta)

    def get_x(self):
        """
        Return x position
        :return: int
        """
        return self.__x

    def get_y(self):
        """
        Return y position
        :return: int
        """
        return self.__y

    def update(self, time_interval):
        """
        Update position of bird after time_interval seconds
        :param time_interval: interval in seconds for computing movement of bird
        :return: None
        """
        self.__x = self.__x + time_interval * self.__xvel
        yvel1 = self.__yvel - time_interval * 9.8
        self.__y = self.__y + time_interval * (self.__yvel + yvel1) / 2.0
        self.__yvel = yvel1

    def print_position(self):
        """
        Output bird position
        :return: None
        """
        print("x pos: ", self.__x)
        print("y pos: ", self.__y)
        print("")


def main():
    time_interval = 0.1

    # create the wall
    wall = Wall(20, 6)

    while not wall.is_destroyed():

        # get the angle and velocity
        theta_degrees = float(input("Enter launch angle: "))
        bird_velocity = float(input("Enter launch velocity (m/s): "))

        # create a bird
        bird = Bird(theta_degrees, bird_velocity)
        hit_ground = False
        hit_wall = False

        while not hit_ground and not hit_wall:
            bird.update(time_interval)

            bird.print_position()

            # check if bird has hit the ground or hit the wall
            if bird.get_y() < 0 and bird.get_x() < wall.get_x():
                print("hit ground")
                hit_ground = True

            elif wall.collide(bird):
                hit_wall = True
                print("hit wall")
                print("wall health:", wall.get_health())

    print("wall destroyed, attack the pigs!!!")


main()








