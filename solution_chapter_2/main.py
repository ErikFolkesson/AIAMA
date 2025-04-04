from environment.vacuum_world import VacuumWorld
from agent.reflex_agent import ReflexAgent

def main():
    # Create a VacuumWorld instance
    grid_size = (1, 2)
    dirt_probability = 0.0

    # Test all possible agent/dirt configurations
    dirt_placement_1 = [(0,1), (0,0)]

    print("Run 1: ")
    vacuum_world = VacuumWorld(grid_size, dirt_probability)
    agent = ReflexAgent(vacuum_world)
    run_simulation(vacuum_world, agent, dirt_placement_1, 5)
    vacuum_world.display_grid()
    print("-------------")


def run_simulation(vacuum_world, agent, dirt_placement, steps = 100):
    if dirt_placement:
        vacuum_world.manual_dirt_placement(dirt_placement)

    for _ in range(steps):
        agent.take_action()
        vacuum_world.simulate_one_time_step()

    score = vacuum_world.get_total_reward()

    print(f"Total Reward: {score}")

if __name__ == "__main__":
    main()
