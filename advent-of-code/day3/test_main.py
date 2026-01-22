# pylint: skip-file
from main import calculate_gamma_rate, calculate_epsilon_rate, convert_binary_to_decimal, calculate_generator_rating, calculate_scrubber_rating


def test_calculate_gamma_rate_1(report):

    assert calculate_gamma_rate(report) == "10110"


def test_calculate_gamma_rate_2():

    assert calculate_gamma_rate(["00100"]) == "00100"


def test_calculate_epsilon_rate_1():

    assert calculate_epsilon_rate("10110") == "01001"


def test_calculate_epsilon_rate_2():

    assert calculate_epsilon_rate("00000000") == "11111111"


def test_convert_binary_to_decimal_1():

    assert convert_binary_to_decimal("01001") == 9


def test_convert_binary_to_decimal_2():

    assert convert_binary_to_decimal("10110") == 22


def test_calculate_generator_rating(report):

    assert calculate_generator_rating(report) == "10111"


def test_calculate_scrubber_rating(report):

    assert calculate_scrubber_rating(report) == "01010"
