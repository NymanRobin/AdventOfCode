from collections import defaultdict


ROTATION_TABLE = {(1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0)}
DIRECTION_TO_ARROW = {(1, 0): "v", (0, -1): "<", (-1, 0): "^", (0, 1): ">"}


def read_input_as_matrix(path):
    matrix = []
    with open(path, mode="r", encoding="UTF-8") as f:
        for line in f:
            row = []
            for pos in line.strip():
                row.append(pos)
            matrix.append(row)
    return matrix


def find_start_position(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "^":
                grid[row][col] == "."
                return (row, col)
    return None


def move_out_of_grid(grid, row, col):
    result = 1
    direction = (-1, 0)
    while True:
        new_row = row + direction[0]
        new_col = col + direction[1]

        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            break

        if grid[new_row][new_col] == "#":
            direction = ROTATION_TABLE[direction]
            continue

        row, col = new_row, new_col
        print(grid[row][col])
        if grid[row][col] == ".":
            result += 1
        grid[row][col] = DIRECTION_TO_ARROW[direction]

    return result


def trick_guard(grid, row, col):
    result = 0
    direction = (-1, 0)
    while True:
        new_row = row + direction[0]
        new_col = col + direction[1]

        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            break

        if grid[new_row][new_col] == "#":
            direction = ROTATION_TABLE[direction]
            continue

        row, col = new_row, new_col
        potential_trap = ROTATION_TABLE[direction]
        result += is_circular(grid, potential_trap, row, col, (row, col))
        print(result)
        # target = DIRECTION_TO_ARROW[potential_trap]
        # result += serach_in_direction(potential_trap, target, row, col)
    return result


def is_circular(grid, direction, row, col, goal):
    seen = set()
    while True:
        new_row = row + direction[0]
        new_col = col + direction[1]
        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            return 0

        if grid[new_row][new_col] == "#":
            direction = ROTATION_TABLE[direction]
            continue

        seen.add((row, col))
        row, col = new_row, new_col
        if (row, col) in seen:
            return 1


# Attempt to figure out if we would end up on the same path did not work somehow
def serach_in_direction(direction, target, row, col):
    while True:
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            return 0
        if grid[row][col] == "#":
            return 0
        if target in grid[row][col]:
            return 1
        row = row + direction[0]
        col = col + direction[1]


if __name__ == "__main__":
    grid = read_input_as_matrix("short-input.txt")
    row, col = find_start_position(grid)
    result = move_out_of_grid(grid, row, col)
    print(row, col)
    print(f"Result of part1: {result}")

    grid = read_input_as_matrix("short-input.txt")
    result = trick_guard(grid, row, col)
    print(row, col)
    print(f"Result of part2: {result}")
