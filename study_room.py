import random as rand


class StudyRoom:

    def __init__(self, lower, upper, count):
        self.total_rooms = count
        self.lower_bound = lower
        self.upper_bound = upper
        self.room_location = set()
        self.configure_location()

    def configure_location(self):
        while len(self.room_location) < self.total_rooms:
            x_loc, y_loc = (rand.randint(self.lower_bound, self.upper_bound),
                            rand.randint(self.lower_bound, self.upper_bound))
            if self.is_valid_location(x_loc, y_loc):
                if x_loc < self.upper_bound and y_loc < self.upper_bound:
                    self.room_location.add((x_loc, y_loc))

    def is_valid_location(self, x_loc, y_loc):
        for existing_loc in self.room_location:
            if (
                    abs(existing_loc[0] - x_loc) < 2 and
                    abs(existing_loc[1] - y_loc) < 2
            ):
                return False  # Overlapping with an existing room
        return True

    def return_location(self):
        return self.room_location
