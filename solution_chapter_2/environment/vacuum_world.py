# environment/vacuum_world.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Patch

class VacuumWorld:
    """
    A class representing the Vacuum World environment.
    The environment is a grid where each cell can either be clean or contain dirt.
    """
    def __init__(self, grid_size: tuple = (2, 1), dirt_probability: float = 0.5):
        """
        Initialize the VacuumWorld with a given grid size and dirt probability.

        :param grid_size: A tuple representing the size of the grid (rows, columns).
        :param dirt_probability: A float representing the probability of each cell containing dirt.
        """
        assert len(grid_size) == 2, "grid_size must be a tuple of two integers"
        assert 0 <= dirt_probability <= 1, "dirt_probability must be between 0 and 1"

        self.grid_size = grid_size
        self.dirt_probability = dirt_probability
        self.grid = np.zeros(grid_size)
        self.total_reward = 0.0
        self.time_step = 0

        self._populate_grid()

    def manual_dirt_placement(self, dirt_positions: list):
        """
        Manually place dirt in the grid at specified positions.

        :param dirt_positions: List of tuples indicating positions to place dirt.
        """
        for pos in dirt_positions:
            if 0 <= pos[0] < self.grid.shape[0] and 0 <= pos[1] < self.grid.shape[1]:
                self.grid[pos] = 1
            else:
                raise ValueError(f"Position {pos} is out of bounds for the grid size {self.grid.shape}.")

    def set_dirt_prob(self, dirt_probability: float):
        """
        Set the probability of dirt appearing in each cell.

        :param dirt_probability: A float representing the probability of each cell containing dirt.
        """
        assert 0 <= dirt_probability <= 1, "dirt_probability must be between 0 and 1"
        self.dirt_probability = dirt_probability

    def get_dirt_prob(self) -> float:
        """
        Get the current dirt probability.

        :return: The current dirt probability.
        """
        return self.dirt_probability

    def _populate_grid(self):
        """
        Populate the grid with dirt based on the dirt probability.
        """
        random_values = np.random.rand(*self.grid.shape)
        self.grid[random_values < self.dirt_probability] = 1

    def display_grid(self, agent_location: tuple = None):
        """
        Display the current state of the grid using matplotlib.
        """
        cmap = mcolors.ListedColormap(['white', 'black'])
        bounds = [0, 1]
        norm = mcolors.BoundaryNorm(bounds, cmap.N)
        plt.imshow(self.grid, cmap=cmap, norm=norm, interpolation='nearest')

        plt.title('Vacuum World Grid')

        if agent_location:
            # Plot the agent's position
            agent_x, agent_y = agent_location
            plt.scatter(agent_y, agent_x, color='red', s=400, label='Agent')

        # Display the total reward
        plt.text(0.5, -0.1, f'Total Reward: {self.total_reward}', ha='center', va='center',
                 transform=plt.gca().transAxes)

        legend_handles = [Patch(color='white', label='No Dirt'),
                          Patch(color='black', label='Dirt')]
        plt.legend(handles=legend_handles, loc='upper right')

        # Remove axis labels
        plt.xticks([])
        plt.yticks([])

        plt.show()

    def get_total_reward(self) -> float:
        """
        Get the total reward accumulated by the agent.

        :return: The total reward.
        """
        return self.total_reward

    def simulate_one_time_step(self):
        """
        Simulate one time step in the environment.
        """
        clean_cells = np.sum(self.grid == 0)
        self.total_reward += clean_cells
        self.time_step += 1

    def get_percept(self, location: tuple) -> bool:
        """
        Get the percept at a given location.

        :param location: A tuple representing the location (row, column).
        :return: True if there is dirt at the location, False otherwise.
        """
        x, y = location
        return self.grid[x, y] == 1

    def suck_location(self, location: tuple):
        """
        Suck dirt at a given location.

        :param location: A tuple representing the location (row, column).
        """
        x, y = location
        self.grid[x, y] = 0