import sys

sys.set_int_max_str_digits(0)
MEM = {}


def read_input(path):
    stones = []
    with open(path, mode="r", encoding="UTF-8") as f:
        for line in f:
            for stone in line.strip().split(" "):
                stones.append(int(stone))
    return stones


def transfrom_stones(stones):
    for _ in range(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                char_stone = str(stone)
                index = len(char_stone) // 2
                first_new_stone = int(char_stone[0:index])
                second_stone = int(char_stone[index:])
                new_stones.append(first_new_stone)
                new_stones.append(second_stone)
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)


def solve_stones(stones):
    result = 0
    for stone in stones:
        result += solve_stone(stone, 75)
    return result


def solve_stone(stone, iteration):
    if iteration == 0:
        return 1
    if (stone, iteration) in MEM:
        return MEM[(stone, iteration)]
    result = 0
    if stone == 0:
        result += solve_stone(1, iteration - 1)
    elif len(str(stone)) % 2 == 0:
        char_stone = str(stone)
        index = len(char_stone) // 2
        first_new_stone = int(char_stone[0:index])
        second_stone = int(char_stone[index:])
        result += solve_stone(first_new_stone, iteration - 1)
        result += solve_stone(second_stone, iteration - 1)
    else:
        result += solve_stone(stone * 2024, iteration - 1)
    MEM[(stone, iteration)] = result
    return result


if __name__ == "__main__":
    stones = read_input("input.txt")
    result = transfrom_stones(stones)
    print(f"Result of part1: {result}")

    # Brute force was not nice for part2 :D
    result = solve_stones(stones)
    print(f"Result of part2: {result}")
