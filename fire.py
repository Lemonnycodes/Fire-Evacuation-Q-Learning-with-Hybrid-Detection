"""
    Table Chair Class to set up table chairs in map grid
"""
# libraries
import random as rand


class Fire:

    def __init__(self, lower, upper, count):
        self.total_fire = count
        self.lower_bound = lower
        self.upper_bound = upper
        self.fire_location = set()
        self.configure_location()
        self.move_directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

    def configure_location(self):
        while len(self.fire_location) < self.total_fire:
            x_loc, y_loc = (rand.randint(self.lower_bound, self.upper_bound),
                            rand.randint(self.lower_bound, self.upper_bound))
            if (self.is_valid_location(x_loc, y_loc) and
                    x_loc < self.upper_bound and y_loc < self.upper_bound):
                self.fire_location.add((x_loc, y_loc))

    def is_valid_location(self, x_loc, y_loc):
        for existing_loc in self.fire_location:
            if (
                    abs(existing_loc[0] - x_loc) < 1 and
                    abs(existing_loc[1] - y_loc) < 1
            ):
                return False  # Overlapping with an existing room
        return True

    def return_location(self):
        return self.fire_location

    def update_location(self, prob=0.5):
        new_fire_locations = set()

        # Spreading fire to adjacent cell
        for x, y in self.fire_location:
            new_fire_locations.add((x, y))
            if rand.uniform(0, 1) < prob:
                dx, dy = rand.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
                new_x, new_y = x + dx, y + dy
                if self.is_valid_location(new_x, new_y):
                    new_fire_locations.add((new_x, new_y))

        # updating fire location
        self.fire_location = new_fire_locations
        return self.fire_location

    def sense_fire(self, sensors_location, people_location):
        # check if the new fire location is sensed by sensor or found by people
        fire_sensed = set()
        for x, y in sensors_location:
            for dx, dy in self.move_directions:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) in self.fire_location:
                    fire_sensed.add((new_x, new_y))

        for x, y in people_location:
            for dx, dy in self.move_directions:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) in self.fire_location:
                    fire_sensed.add((new_x, new_y))

        return fire_sensed
