# agent/reflex_agent.py

from environment.vacuum_world import VacuumWorld
import random

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
        if self.env.get_percept(self.location):
            self.env.suck_location(self.location)
        else:
            # Randomly choose to move left or right first
            direction = random.choice([True, False])
            if direction:
                new_location = self._move_right()
                if not self._new_location_valid(new_location):
                    new_location = self._move_left()
            else:
                new_location = self._move_left()
                if not self._new_location_valid(new_location):
                    new_location = self._move_right()

            self.location = new_location

    def _move_right(self):
        new_location = (self.location[0], self.location[1] + 1)
        return new_location

    def _move_left(self):
        new_location = (self.location[0], self.location[1] - 1)
        return new_location

    def _new_location_valid(self, new_location):
        return 0 <= new_location[1] < self.env.grid_size[1]

    def get_location(self):
        return self.location