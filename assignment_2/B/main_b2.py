from collections import deque


def find_exit_time(labyrinth_map, initial_positions, speeds):
    queue = deque()
    visited = set()

    # Add initial positions of wizards to the queue
    for i in range(len(initial_positions)):
        position = initial_positions[i]
        speed = speeds[i]
        queue.append((position, 0, speed))  # (position, time, speed)
        visited.add(position)

    while queue:
        position, time, speed = queue.popleft()

        # Check if the current position is the exit
        if position == 'exit':
            return time

        # Explore neighboring corridors
        for neighbor in labyrinth_map[position]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_time = time + 1 + 1 / speed  # 1 minute to move to the neighbor + additional time based on speed
                queue.append((neighbor, new_time, speed))

    # If no wizard reaches the exit, return None
    return None


# Example usage
labyrinth_map = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'exit'],
    'E': ['C', 'exit'],
    'exit': []
}

initial_positions = ['A', 'B', 'C']
speeds = [2, 1, 3]

winner = None
min_time = float('inf')

for i in range(len(initial_positions)):
    exit_time = find_exit_time(labyrinth_map, initial_positions, speeds)
    if exit_time is not None and exit_time < min_time:
        min_time = exit_time
        winner = i

if winner is not None:
    print(f"Wizard {winner + 1} will reach the exit first.")
else:
    print("No wizard reaches the exit.")

