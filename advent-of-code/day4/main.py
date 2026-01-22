def read_input(filename: str) -> list[str]:
    """Read .txt input"""
    with open(filename, "r") as f:
        return f.readlines()


if __name__ == "__main__":

    input = read_input("input.txt")
    draw = input[0][:-1].split(",")

    boards = [i for i in input[1:] if i != '\n']
    print(boards)
