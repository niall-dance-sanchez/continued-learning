"""Advent of Code Day 3"""


def read_input(filename: str) -> list[str]:
    """Read .txt input"""
    with open(filename, "r") as f:
        return f.readlines()


def calculate_gamma_rate(binary_list: list[str]) -> str:
    """Calculates the gamma rate from a list of binary numbers."""

    gamma_rate = ""

    for i in range(len(binary_list[0])):
        counter = {"0": 0, "1": 0}
        for b in binary_list:
            counter[b[i]] += 1
        gamma_rate += max(counter, key=counter.get)

    return gamma_rate


def calculate_epsilon_rate(gamma_rate: str) -> str:
    """Calculates the epsilon rate from a gamma rate string."""

    epsilon_rate = ""
    for num in gamma_rate:
        epsilon_rate += "1" if num == "0" else "0"
    return epsilon_rate


def convert_binary_to_decimal(binary_code: str) -> int:

    value = 0
    for i in range(len(binary_code)):
        value += int(binary_code[::-1][i]) * 2**i

    return value


def calculate_generator_rating(binary_list: list[str]) -> str:

    generator_rating = ""

    values = [i for i in range(len(binary_list))]

    for i in range(len(binary_list[0])):
        counter = {"0": 0, "1": 0}

        for j in values:
            counter[binary_list[j][i]] += 1

        if counter["0"] == counter["1"]:
            mode = '1'
        else:
            mode = max(counter, key=counter.get)

        generator_rating += mode

        values = [j for j in values
                  if binary_list[j][i] == mode]

    return generator_rating


def calculate_scrubber_rating(binary_list: list[str]) -> str:

    scrubber_rating = ""

    values = [i for i in range(len(binary_list))]

    for i in range(len(binary_list[0])):
        counter = {"0": 0, "1": 0}

        if len(values) == 1:
            scrubber_rating = binary_list[values[0]]
        else:
            for j in values:
                counter[binary_list[j][i]] += 1

            if counter["0"] == counter["1"]:
                mode = '0'
            else:
                mode = min(counter, key=counter.get)

            scrubber_rating += mode

            values = [j for j in values
                      if binary_list[j][i] == mode]

    return scrubber_rating


if __name__ == "__main__":
    input = read_input("input.txt")

    clean_input = []

    for i in range(len(input)-1):
        clean_input.append(input[i][:-1])
    clean_input.append(input[-1])

    gamma_rate = calculate_gamma_rate(clean_input)
    epsilon_rate = calculate_epsilon_rate(gamma_rate)
    gamma_decimal = convert_binary_to_decimal(gamma_rate)
    epsilon_decimal = convert_binary_to_decimal(epsilon_rate)
    answer = gamma_decimal * epsilon_decimal
    print(answer)

    generator = calculate_generator_rating(clean_input)
    scrubber = calculate_scrubber_rating(clean_input)
    generator_decimal = convert_binary_to_decimal(generator)
    scrubber_decimal = convert_binary_to_decimal(scrubber)
    answer = generator_decimal * scrubber_decimal
    print(answer)
