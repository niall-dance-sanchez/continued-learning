# pylint: skip-file

from main import sum_sub_commands, sum_sub_commands_with_aim


def test_sum_sub_commands_1():

    assert sum_sub_commands(["forward 5",
                             "down 5",
                             "forward 8",
                             "up 3",
                             "down 8",
                             "forward 2"]) == [15, 10]


def test_sum_sub_commands_2():

    assert sum_sub_commands(["forward 5",
                             "forward 5"]) == [10, 0]


def test_sum_sub_commands_with_aim_1():

    assert sum_sub_commands_with_aim(["forward 5",
                                      "down 5",
                                      "forward 8",
                                      "up 3",
                                      "down 8",
                                      "forward 2"]) == [15, 60]


def test_sum_sub_commands_with_aim_2():

    assert sum_sub_commands_with_aim(["forward 5",
                                      "forward 5"]) == [10, 0]
