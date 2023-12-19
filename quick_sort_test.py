from quick_sort import quick_sort


def test_quick_sort_1():
    nums = [8, 7, 2, 1, 0, 9, 6]
    expected = [0, 1, 2, 6, 7, 8, 9]
    quick_sort(nums)
    assert nums == expected


def test_quick_sort_2():
    nums = [-2, 45, 0, 11, -9]
    expected = [-9, -2, 0, 11, 45]
    quick_sort(nums)
    assert nums == expected


def test_quick_sort_3():
    nums = [1]
    expected = [1]
    quick_sort(nums)
    assert nums == expected


def test_quick_sort_4():
    nums = []
    expected = []
    quick_sort(nums)
    assert nums == expected
