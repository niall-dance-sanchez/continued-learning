"""Advent of code day 2."""


def read_input(filename: str) -> list[str]:
    """Read .txt input"""
    with open(filename, "r") as f:
        return f.readlines()


def sum_sub_commands(commands: list[str]) -> list[int]:
    """Given a list of commands, returns the final horizontal position and depth."""

    position = [0, 0]
    for c in commands:
        if c[0] == 'f':
            position[0] += int(c.split()[1])
        elif c[0] == 'd':
            position[1] += int(c.split()[1])
        elif c[0] == 'u':
            position[1] -= int(c.split()[1])

    return position


def sum_sub_commands_with_aim(commands: list[str]) -> list[int]:
    """Given a list of commands, returns the final horizontal position and depth."""

    position = [0, 0]
    aim = 0
    for c in commands:
        if c[0] == 'f':
            position[0] += int(c.split()[1])
            position[1] += aim * int(c.split()[1])
        elif c[0] == 'd':
            aim += int(c.split()[1])
        elif c[0] == 'u':
            aim -= int(c.split()[1])

    return position


if __name__ == "__main__":
    input = read_input("input.txt")

    clean_input = []

    for i in range(len(input)-1):
        clean_input.append(input[i][:-1])
    clean_input.append(input[-1])

    position = sum_sub_commands(clean_input)
    answer1 = position[0] * position[1]
    print(answer1)

    position = sum_sub_commands_with_aim(clean_input)
    answer2 = position[0] * position[1]
    print(answer2)
