import numpy as np
import heapq as heap

class Astar:
    def __init__(self, fire, row, col, start, goal, room, obstacles):
        self.fire = fire
        self.rows = row
        self.cols = col
        self.base_cost = np.zeros((self.rows, self.cols))
        self.goal = goal
        self.room = room
        self.start = start
        self.obstacles = obstacles
        self.g_score = {}
        self.base_cost_cal()

    def neighbours(self, curr_loc):
        x, y = curr_loc
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbour = {}

        for dx, dy in directions:
            row = x + dx
            col = y + dy

            if 0 <= row < self.rows and 0 <= col < self.cols:
                if curr_loc not in neighbour:
                    neighbour[curr_loc] = [(row, col)]
                else:
                    neighbour[curr_loc].append((row, col))

        return neighbour

    def path_finding(self):
        open_grid = []
        heap.heappush(open_grid, (0, self.start))
        closed_grid = set()
        heap.heapify(open_grid)

        self.g_score[self.start] = 0

        while open_grid:
            element = heap.heappop(open_grid)
            current_node = element[1]

            if current_node == self.goal:
                return self.reconstruct_path()

            closed_grid.add(current_node)

            neighbours = self.neighbours(current_node)
            for neighbor in neighbours[current_node]:
                if neighbor in closed_grid:
                    continue

                tentative_g_score = self.g_score[current_node] + self.distance(current_node, neighbor)
                heuristic_h_score = self.distance(neighbor, self.goal)
                total_f_score = tentative_g_score + heuristic_h_score + self.base_cost[neighbor]

                if (neighbor not in [item[1] for item in open_grid] or
                        tentative_g_score < self.g_score.get(neighbor, float('inf'))):
                    # Update g, h, and f scores
                    self.g_score[neighbor] = tentative_g_score

                    # Add the neighbor to the open set
                    heap.heappush(open_grid, (total_f_score, neighbor))

    def reconstruct_path(self):
        current_node = self.goal
        path = [current_node]

        while current_node != self.start:
            neighbors = self.neighbours(current_node).get(current_node, [])  # Use get to handle missing keys
            if not neighbors:
                break

            current_node = min(neighbors, key=lambda x: self.g_score.get(x, float('inf')))
            path.append(current_node)

        path.reverse()
        return path

    @staticmethod
    def distance(current_node, goal_node):
        curr_x, curr_y = current_node
        goal_x, goal_y = goal_node
        return abs(curr_x - goal_x) + abs(curr_y - goal_y)

    def base_cost_cal(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) in self.fire or (row, col) in self.room or (row, col) in self.obstacles:
                    self.base_cost[(row, col)] = 1000
                elif (row, col) == self.goal:
                    self.base_cost[(row, col)] = 0
                else:
                    self.base_cost[(row, col)] = 2
