from collections import deque

def print_maze(maze):
    for row in maze:
        print("".join(row))

def solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start, [start])])  # Queue stores (current_position, path)

    while queue:
        (x, y), path = queue.popleft()

        # Check if we reached the end
        if (x, y) == end:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check boundaries and if cell is walkable and not visited
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != "#" and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None  # No path found

# Example maze
maze = [
    ["S", ".", ".", "#", ".", ".", "."],
    [".", "#", ".", "#", ".", "#", "."],
    [".", "#", ".", ".", ".", "#", "."],
    [".", ".", "#", "#", ".", "#", "."],
    ["#", ".", "#", "E", ".", ".", "."],
]

start = (0, 0)  # Starting point (row, column)
end = (4, 3)    # Ending point (row, column)

print("Maze:")
print_maze(maze)

path = solve_maze(maze, start, end)

if path:
    print("\nPath Found:")
    for x, y in path:
        if maze[x][y] not in ("S", "E"):  # Avoid overwriting Start (S) and End (E)
            maze[x][y] = "O"
    print_maze(maze)
else:
    print("\nNo Path Found!")
