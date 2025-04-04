from environment.vacuum_world import VacuumWorld
from agent.reflex_agent import ReflexAgent

def main():
    """
    Main function to test all possible agent/dirt configurations in the VacuumWorld.
    """
    # Define the grid size and dirt probability
    grid_size = (1, 2)
    dirt_probability = 0.0

    # List of dirt placements and corresponding run labels
    dirt_placements = [
        ([(0, 0)], "Run 1"),
        ([(0, 1)], "Run 2"),
        ([(0, 1), (0, 0)], "Run 3"),
        (None, "Run 4")
    ]

    # Run the simulation for each dirt placement
    for dirt_placement, run_label in dirt_placements:
        print(f"{run_label}: ")
        run_vacuum_simulation(grid_size, dirt_probability, dirt_placement)
        print("-------------")


def run_vacuum_simulation(grid_size, dirt_probability, dirt_placement, steps=10):
    """
    Run the vacuum simulation with the given parameters.

    :param grid_size: Tuple indicating the size of the grid.
    :param dirt_probability: Probability of dirt being present in the grid.
    :param dirt_placement: List of tuples indicating positions to place dirt manually.
    :param steps: Number of steps to run the simulation.
    """
    # Create a VacuumWorld instance
    vacuum_world = VacuumWorld(grid_size, dirt_probability)
    # Create a ReflexAgent instance
    agent = ReflexAgent(vacuum_world)
    # Run the simulation
    run_simulation(vacuum_world, agent, dirt_placement, steps)
    # Display the grid
    vacuum_world.display_grid(agent.get_location())


def run_simulation(vacuum_world, agent, dirt_placement, steps=10):
    """
    Run the simulation for a specified number of steps.

    :param vacuum_world: Instance of the VacuumWorld.
    :param agent: Instance of the ReflexAgent.
    :param dirt_placement: List of tuples indicating positions to place dirt manually.
    :param steps: Number of steps to run the simulation.
    """
    # Manually place dirt if specified
    if dirt_placement:
        vacuum_world.manual_dirt_placement(dirt_placement)

    # Run the simulation for the given number of steps
    for _ in range(steps):
        agent.take_action()
        vacuum_world.simulate_one_time_step()

    # Print the total reward
    score = vacuum_world.get_total_reward()
    print(f"Total Reward: {score}")


if __name__ == "__main__":
    main()