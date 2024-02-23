"""
    Table Chair Class to set up table chairs in map grid
"""
import random as rand


class People:

    def __init__(self, lower, upper, count):
        self.total_people = count
        self.lower_bound = lower
        self.upper_bound = upper
        self.people_location = set()
        self.configure_location()

    def configure_location(self):
        while len(self.people_location) < self.total_people:
            x_loc, y_loc = (rand.randint(self.lower_bound, self.upper_bound),
                            rand.randint(self.lower_bound, self.upper_bound))
            if (self.is_valid_location(x_loc, y_loc) and
                    x_loc < self.upper_bound and y_loc < self.upper_bound):
                self.people_location.add((x_loc, y_loc))

    def is_valid_location(self, x_loc, y_loc):
        for existing_loc in self.people_location:
            if (
                    abs(existing_loc[0] - x_loc) < 2 and
                    abs(existing_loc[1] - y_loc) < 2
            ):
                return False  # Overlapping with an existing room
        return True

    def return_location(self):
        return self.people_location
