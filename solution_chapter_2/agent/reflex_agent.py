# agent/reflex_agent.py

from environment.vacuum_world import VacuumWorld
import random
import numpy as np

class ReflexAgent:
    """
    A simple reflex agent for the Vacuum World environment.
    The agent perceives its current location and decides to either suck dirt or move left/right.
    """
    def __init__(self, env: VacuumWorld):
        """
        Initialize the ReflexAgent with the given environment.

        :param env: An instance of the VacuumWorld environment.
        """
        self.location = (0, 0)
        self.env = env

    def take_action(self):
        """
        Perform an action based on the current percept.
        If there is dirt at the current location, suck it.
        Otherwise, randomly move left or right within the grid bounds.
        """
        if self.env.get_percept():
            self.env.suck_location(self.location)
        else:
            # Randomly choose to move left or right first
            direction = random.choice([True, False])
            self.env.move(direction)