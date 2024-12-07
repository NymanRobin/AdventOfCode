def read_input(path):
    lines = []
    with open(path, mode="r", encoding="UTF-8") as f:
        for line in f:
            row = []
            goal, rest = line.split(":")
            row.append(goal)
            for num in rest.strip().split(" "):
                row.append(int(num))
            lines.append(row)
    return lines


def get_total(lines, part2=False):
    result = 0
    for line in lines:
        target = int(line[0])
        if is_solvable(1, line[1], target, line[1:], part2):
            result += target
    return result


def is_solvable(index, total, target, nums, part2=False):
    if total == target and index == len(nums):
        return True
    if total > target:
        return False
    if index == len(nums):
        return False

    next_num = nums[index]

    if is_solvable(index + 1, total + next_num, target, nums, part2):
        return True

    # Does not seem like santa is good at math operation orders :)
    if is_solvable(index + 1, total * next_num, target, nums, part2):
        return True

    if part2:
        concatenated = int(f"{total}{next_num}")
        if is_solvable(index + 1, concatenated, target, nums, part2):
            return True

    return False


if __name__ == "__main__":
    lines = read_input("input.txt")
    result = get_total(lines)
    print(f"Result of part1: {result}")

    lines = read_input("input.txt")
    result = get_total(lines, part2=True)
    print(f"Result of part2: {result}")
