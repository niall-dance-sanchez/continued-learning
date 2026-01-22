# pylint: skip-file

from main import check_depth_increase, count_depth_increases, sum_windows


def test_basic_check_depth_increase():

    assert check_depth_increase(199, 200) == True


def test_basic_check_depth_increase_2():

    assert check_depth_increase(200, 208) == True


def test_basic_check_depth_increase_3():

    assert check_depth_increase(210, 200) == False


def test_basic_count_depth_increases_1():

    assert count_depth_increases([199,
                                  200,
                                  208,
                                  210,
                                  200,
                                  207,
                                  240,
                                  269,
                                  260,
                                  263]) == 7


def test_basic_count_depth_increases_2():

    assert count_depth_increases([1, 2]) == 1


def test_basic_count_depth_increases_3():

    assert count_depth_increases([3, 2, 0, 0, 0]) == 0


def test_basic_sum_windows_1():

    assert sum_windows([199,
                        200,
                        208,
                        210,
                        200,
                        207,
                        240,
                        269,
                        260,
                        263]) == [607, 618, 618, 617, 647, 716, 769, 792]


def test_basic_sum_windows_2():

    assert sum_windows([1, 2, 3]) == [6]
