from collections import defaultdict


def read_input(path):
    matrix = []
    with open(path, mode="r", encoding="UTF-8") as f:
        for line in f:
            row = []
            for pos in line.strip():
                row.append(pos)
            matrix.append(row)
    return matrix


def create_signal_map(matrix):
    signal_map = defaultdict(list)
    for r, row in enumerate(matrix):
        for c, element in enumerate(row):
            if element != ".":
                signal_map[element].append((r, c))
    return signal_map


def find_antinodes(signal_map, grid):
    result = 0
    nodes = set()
    for _, position_list in signal_map.items():
        for index, position in enumerate(position_list):
            i = index + 1
            while i < len(position_list):
                p1, p2 = get_inferance_points(position, position_list[i], grid)
                if p1 and p1 not in nodes:
                    result += 1
                    nodes.add(p1)
                if p2 and p2 not in nodes:
                    result += 1
                    nodes.add(p2)
                i += 1
    return result


def get_inferance_points(tower1, tower2, grid):
    inferance_p1 = None
    inferance_p2 = None
    inferance_p1 = (
        tower1[0] + tower1[0] - tower2[0],
        tower1[1] + tower1[1] - tower2[1],
    )
    inferance_p2 = (
        tower2[0] + tower2[0] - tower1[0],
        tower2[1] + tower2[1] - tower1[1],
    )

    if inferance_p1[0] < 0 or inferance_p1[0] >= len(grid):
        inferance_p1 = None

    if inferance_p1 and (inferance_p1[1] < 0 or inferance_p1[1] >= len(grid[0])):
        inferance_p1 = None

    if inferance_p2[0] < 0 or inferance_p2[0] >= len(grid):
        inferance_p2 = None

    if inferance_p2 and (inferance_p2[1] < 0 or inferance_p2[1] >= len(grid[0])):
        inferance_p2 = None

    return inferance_p1, inferance_p2


def find_extended_antinodes(signal_map, grid):
    result = 0
    nodes = set()
    for _, position_list in signal_map.items():
        for index, position in enumerate(position_list):
            i = index + 1
            while i < len(position_list):
                node_pos = get_list_of_inferance_points(
                    position, position_list[i], grid
                )
                print(node_pos)
                for node in node_pos:
                    if node not in nodes:
                        grid[node[0]][node[1]] = "#"
                        print(f"Adding node {node}")
                        result += 1
                        nodes.add(node)
                i += 1
    return result


def get_list_of_inferance_points(tower1, tower2, grid):
    result = []

    x1_delta = tower1[0] - tower2[0]
    y1_delta = tower1[1] - tower2[1]

    x2_delta = tower2[0] - tower1[0]
    y2_delta = tower2[1] - tower1[1]

    inferance_p1 = (
        tower1[0],
        tower1[1],
    )
    inferance_p2 = (
        tower2[0],
        tower2[1],
    )

    while (
        inferance_p1[0] >= 0
        and inferance_p1[0] < len(grid)
        and (inferance_p1[1] >= 0 and inferance_p1[1] < len(grid[0]))
    ):
        result.append(inferance_p1)
        inferance_p1 = (
            inferance_p1[0] + x1_delta,
            inferance_p1[1] + y1_delta,
        )

    while (
        inferance_p2[0] >= 0
        and inferance_p2[0] < len(grid)
        and (inferance_p2[1] >= 0 and inferance_p2[1] < len(grid[0]))
    ):
        result.append(inferance_p2)
        inferance_p2 = (
            inferance_p2[0] + x2_delta,
            inferance_p2[1] + y2_delta,
        )

    return result


if __name__ == "__main__":
    matrix = read_input("input.txt")
    signal_map = create_signal_map(matrix)
    result = find_antinodes(signal_map, matrix)
    print(f"Result of part1: {result}")

    result = find_extended_antinodes(signal_map, matrix)
    print(f"Result of part2: {result}")
