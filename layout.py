# import libraries
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.patches import Ellipse, Rectangle, Circle
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.animation import FuncAnimation

class Layout:

    def __init__(self, row, col, people, study_room, table_chair, fire_exits, sensors):
        self.row = row
        self.col = col
        self.grid = np.zeros(shape=(row, col))
        self.people = people
        self.study_room = study_room
        self.table_chair = table_chair
        self.fire_exits = fire_exits
        self.sensors = sensors
        self.place_objects()
        self.red_fire_image = mpimg.imread('fire.png')
        self.blue_fire_image = mpimg.imread('blue_fire.png')
        self.table = mpimg.imread('table.png')
        self.room = mpimg.imread('room.png')
        self.exit = mpimg.imread('exit.png')
        self.sensor = mpimg.imread('sensor.png')

    def place_objects(self):
        for loc in self.people:
            self.grid[loc] = 2

        for x_loc, y_loc in self.study_room:
            self.grid[(x_loc, y_loc)] = 2

        for x_loc, y_loc in self.table_chair:
            self.grid[(x_loc, y_loc)] = 2

        for x_loc, y_loc in self.fire_exits:
            self.grid[(x_loc, y_loc)] = 2

        for x_loc, y_loc in self.sensors:
            self.grid[(x_loc, y_loc)] = 2

    def object_plotting(self, fire_location, people_locations_list):
        plot_map_color = ListedColormap(['white', 'blue', 'brown', 'white'])

        plt.imshow(self.grid, cmap=plot_map_color, origin='upper')

        def update(frame):
            x, y = people_locations_list[frame]
            plt.gca().add_patch(Circle((x, y), 0.1, edgecolor='red', facecolor='none'))

            for x, y in self.study_room:
                room_imagebox = OffsetImage(self.room, zoom=0.2)
                ab = AnnotationBbox(room_imagebox, (x, y), frameon=False, xycoords='data', boxcoords='data')
                plt.gca().add_artist(ab)
            for x, y in self.table_chair:
                table_imagebox = OffsetImage(self.table, zoom=0.2)
                ab = AnnotationBbox(table_imagebox, (x, y), frameon=False, xycoords='data', boxcoords='data')
                plt.gca().add_artist(ab)
            for x, y in self.fire_exits:
                fire_imagebox = OffsetImage(self.exit, zoom=0.02)
                ab = AnnotationBbox(fire_imagebox, (x, y), frameon=False, xycoords='data', boxcoords='data')
                plt.gca().add_artist(ab)
            for x, y in self.sensors:
                sensor_imagebox = OffsetImage(self.sensor, zoom=0.05)
                ab = AnnotationBbox(sensor_imagebox, (x, y), frameon=False, xycoords='data', boxcoords='data')
                plt.gca().add_artist(ab)
            for x, y in fire_location:
                fire_imagebox = OffsetImage(self.red_fire_image, zoom=0.08)
                ab = AnnotationBbox(fire_imagebox, (x, y), frameon=False, xycoords='data', boxcoords="data")
                plt.gca().add_artist(ab)

            plt.grid(color='gray', linestyle='dotted', linewidth=0.5)
            plt.xticks(np.arange(0, self.col + 1, 1))
            plt.yticks(np.arange(0, self.row + 1, 1))
            plt.title('Fire Location')

        # Create an animation object
        num_frames = len(people_locations_list)
        anim = FuncAnimation(plt.gcf(), update, frames=num_frames, interval=500, repeat=False)

        plt.show()
