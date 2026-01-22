"""Advent of code day 1."""

# pylint:disable=redefined-outer-name,unspecified-encoding


def read_input(filename: str) -> list[str]:
    """Read .txt input"""
    with open(filename, "r") as f:
        return f.readlines()


def check_depth_increase(old_depth: int, new_depth: int) -> bool:
    """Compares two depths, returns True if the depth increases, False otherwise."""

    if new_depth > old_depth:
        return True
    return False


def count_depth_increases(depth_measurements: list[int]) -> int:
    """Given a list of depth measurements, counts the number of increases."""
    count = 0
    for i in range(1, len(depth_measurements)):
        if check_depth_increase(depth_measurements[i-1], depth_measurements[i]):
            count += 1
    return count


def sum_windows(depth_measurements: list[int]) -> list[int]:
    """Given a list of depth measurements, finds the sum of each three measurement window"""

    windows = []
    for i in range(2, len(depth_measurements)):
        windows.append(depth_measurements[i-2]
                       + depth_measurements[i-1]
                       + depth_measurements[i])
    return windows


if __name__ == "__main__":
    task_input = read_input("input.txt")

    clean_input = []

    for i in range(len(task_input)-1):
        clean_input.append(int(task_input[i][:-1]))
    clean_input.append(int(task_input[-1]))

    print(count_depth_increases(clean_input))
    windows = sum_windows(clean_input)
    print(count_depth_increases(windows))
