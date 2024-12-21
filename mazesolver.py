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

def create_maze(rows, cols, obstacles):
    # Initialize the maze with empty cells
    maze = [["." for _ in range(cols)] for _ in range(rows)]

    # Place obstacles in the maze
    for x, y in obstacles:
        maze[x][y] = "#"

    return maze

# Input the maze dimensions
rows = int(input("Enter the number of rows in the maze: "))
cols = int(input("Enter the number of columns in the maze: "))

# Input obstacles
num_obstacles = int(input("Enter the number of obstacles: "))
obstacles = []
print("Enter the obstacle positions as row and column indices (e.g., 1 2):")
for _ in range(num_obstacles):
    x, y = map(int, input().split())
    obstacles.append((x, y))

# Input start and end points
start = tuple(map(int, input("Enter the start point as row and column indices (e.g., 0 0): ").split()))
end = tuple(map(int, input("Enter the end point as row and column indices (e.g., 4 3): ").split()))

# Create the maze
maze = create_maze(rows, cols, obstacles)
maze[start[0]][start[1]] = "S"
maze[end[0]][end[1]] = "E"

print("\nMaze:")
print_maze(maze)

# Solve the maze
path = solve_maze(maze, start, end)
if path:
    print("\nPath Found:")
    for x, y in path:
        if maze[x][y] not in ("S", "E"):  # Avoid overwriting Start (S) and End (E)
            maze[x][y] = "O"
    print_maze(maze)
else:
    print("\nNo Path Found!") 
