# Importing necessary libraries
import random as rand
from fire import Fire
from sensors import Sensors
from table_chair import TableChair
from study_room import StudyRoom
from people import People
from exits import Exists
from layout import Layout
from qlearning import QLearning
from astar import Astar


# Defining the main class for pathfinding
class Path:
    def __init__(self):
        # Setup grid size
        self.ROWS = 12
        self.COLS = 12

        # Setup sensors
        rand.seed(350)
        self.sensor = Sensors(lower=1, upper=self.ROWS, count=rand.randint(4, 5))
        self.sensors_location = self.sensor.return_location()

        # Setup fire
        self.fire = Fire(lower=1, upper=self.ROWS, count=rand.randint(4, 5))
        self.fire_location = self.fire.return_location()

        # Setup tables and chairs
        self.tab_chair = TableChair(lower=1, upper=self.ROWS, count=rand.randint(4, 5))
        self.tab_chair_location = self.tab_chair.return_location()

        # Setup study rooms
        self.room = StudyRoom(lower=1, upper=self.ROWS, count=rand.randint(4, 5))
        self.study_room_location = self.room.return_location()

        # Setup people
        self.people = People(lower=1, upper=self.ROWS, count=rand.randint(4, 5))
        self.people_location = self.people.return_location()
        self.total_people_count = self.alive_people = len(self.people_location)
        self.dead_people = 0

        # Setup exits
        self.exit_loc = Exists(lower=1, upper=self.ROWS, count=rand.randint(1, 1))
        self.exits_location = self.exit_loc.return_location()

        # Setup layout
        self.layout = Layout(row=self.ROWS, col=self.COLS, people=[(0, 0)],
                             study_room=self.study_room_location, table_chair=self.tab_chair_location,
                             fire_exits=self.exits_location, sensors=self.sensors_location)

    # Method for hybrid pathfinding using A* and Q-learning
    def hybrid_path_finding(self):
        for people in self.people_location:
            final_path = []
            for exit_loc in self.exits_location:
                # A* pathfinding algorithm
                astar = Astar(fire=self.fire_location, row=self.ROWS, col=self.COLS, goal=exit_loc, start=people,
                              room=self.study_room_location, obstacles=self.tab_chair_location)

                astar_path = astar.path_finding()
                avoid_loc = []

                # random fire spread
                self.fire_location = self.fire.update_location()

                # Checking if the current person is not in a fire location
                if people not in self.fire_location:
                    for i in range(len(astar_path)):
                        next_loc = astar_path[i + 1] if i < len(astar_path) - 1 else None

                        # Checking for obstacles and fire in the path
                        if (next_loc in self.fire_location or next_loc in self.study_room_location or
                                next_loc in self.tab_chair_location):
                            start = astar_path[i]
                            next_index = i + 1
                            goal = astar_path[next_index]

                            # Finding a safe path using Q-learning
                            while goal in self.fire_location:
                                next_index += 1
                                if next_index < len(astar_path):
                                    goal = astar_path[next_index]
                            new_diverted_path = self.replan_path(start, goal)
                            avoid_loc.append(astar_path[i])
                            avoid_loc.append(astar_path[i + 1])
                            avoid_loc.append(astar_path[next_index])

                            # Appending the safe path to the final path
                            for path in new_diverted_path:
                                if path not in self.fire_location:
                                    final_path.append(path)
                        else:
                            # Appending path to the final path if there are no obstacles
                            if astar_path[i] not in avoid_loc:
                                final_path.append(astar_path[i])
                    # Plotting the path on the layout
                    self.layout.object_plotting(self.fire_location, final_path)

    # Method to replan the path using Q-learning
    def replan_path(self, start, remaining_path):
        q_learn = QLearning(grid_size=self.ROWS, row=start[0], col=start[1], exit_location=remaining_path,
                            room=self.study_room_location, table=self.tab_chair_location,
                            fire_location=self.fire_location)
        q_learn.train(start_state=start, num_episodes=50000)
        q_learned_path = q_learn.predict_path(start, remaining_path)
        return q_learned_path


# Entry point of the program
if __name__ == '__main__':
    main_logic = Path()
    main_logic.hybrid_path_finding()
