import numpy as np
import random as rand


class QLearning:
    def __init__(self, grid_size, row, col, exit_location, fire_location, table, room, learning_rate=0.1,
                 discount_factor=0.2, exploration_prob=0.5):
        self.grid_size = grid_size
        self.start_row = row
        self.start_col = col
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_prob = exploration_prob
        self.table = table
        self.room = room
        self.num_actions = 4
        self.fire_locations = fire_location
        self.exits_locations = exit_location

        # Initialize Q-values for each state-action pair
        self.q_values = np.zeros((grid_size, grid_size, self.num_actions))

    def select_action(self, state):
        # Epsilon-greedy policy for action selection
        if rand.uniform(0, 1) < self.exploration_prob:
            return rand.randint(0, self.num_actions-1)
        else:
            return np.argmax(self.q_values[state])

    def update_q_values(self, state, reward, next_state, action):
        current_value = self.q_values[state][action]
        max_future_value = np.max(self.q_values[next_state])
        new_value = current_value + self.learning_rate * (reward + self.discount_factor * max_future_value -
                                                          current_value)
        self.q_values[state][action] = new_value

    def train(self, start_state, num_episodes):
        for episode in range(num_episodes):
            # Initialize state for each person
            current_state = start_state

            while True:
                # select the action
                action = self.select_action(current_state)

                # Simulate the environment (move the person)
                new_state, reward, is_done = self.take_action(current_state, action)

                # Update Q-values
                self.update_q_values(current_state, reward, new_state, action)

                # Move to the next state
                current_state = new_state

                if is_done:
                    break

    def take_action(self, current_state, action):
        # Move in the chosen action direction
        new_state = current_state

        if action == 0:  # Move Up
            new_state = (max(0, new_state[0] - 1), new_state[1])
        elif action == 1:  # Move Down
            new_state = (min(new_state[0] + 1, self.grid_size - 1), new_state[1])
        elif action == 2:  # Move Left
            new_state = (new_state[0], max(0, new_state[1] - 1))
        elif action == 3:  # Move Right
            new_state = (new_state[0], min(self.grid_size - 1, new_state[1] + 1))

        # Check if the new position is valid
        if new_state in self.fire_locations:
            reward = -50
            is_done = True
        elif new_state == self.exits_locations:
            reward = 100
            is_done = True
        elif new_state in self.table:
            reward = -50
            is_done = True
        elif new_state in self.room:
            reward = -50
            is_done = True
        else:
            reward = -1
            is_done = False

        return new_state, reward, is_done

    def predict_path(self, initial_state, escape_state):
        current_state = initial_state
        path = [current_state]
        while current_state != escape_state:
            action = np.argmax(self.q_values[current_state])
            next_state, reward, is_done = self.take_action(current_state, action)
            current_state = next_state
            path.append(current_state)
        return path
