"""Testing random grouping"""
from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers


import pytest
from gatorgrouper.utils import group_random
from gatorgrouper.utils import group_rrobin


def test_group_random1():
    """Testing that the group_random() function creates the
        appropriate number of groups with the appropriate number"""
    lst = [
        "Austin",
        "Dan",
        "Angie",
        "Cullen",
        "Chase",
        "Vinny",
        "Nick",
        "Jeff",
        "James",
        "Kelly",
        "Nikki",
        "Robert",
    ]
    lst2 = ["Dan", "Angie", "Austin", "Izaak", "Nick", "Jeff"]
    group_size = 3
    group_size2 = 2
    num_group = 2
    num_group2 = 3
    actual_output = group_random.group_random_group_size(lst, group_size)
    actual_output2 = group_random.group_random_group_size(lst2, group_size2)
    actual_output3 = group_random.group_random_num_group(lst, num_group)
    actual_output4 = group_random.group_random_num_group(lst2, num_group2)

    assert len(actual_output) == 4
    assert len(actual_output[0]) == 3
    assert len(actual_output2) == 3
    assert len(actual_output2[0]) == 2
    assert len(actual_output3) == 2
    assert len(actual_output3[0]) == 6
    assert len(actual_output4) == 3
    assert len(actual_output4[0]) == 2


@given(group_size=integers(min_value=1, max_value=3))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def hypothesis_test_group_random1(group_size):
    """this hypothesis test can generate the group numbers and test if it pass
        the requirements"""
    lst = [
        "Austin",
        "Dan",
        "Angie",
        "Cullen",
        "Chase",
        "Vinny",
        "Nick",
        "Jeff",
        "James",
        "Kelly",
        "Nikki",
        "Robert",
    ]
    lst2 = ["Dan", "Angie", "Austin", "Izaak", "Nick", "Jeff"]
    size_count = group_size
    actual_output = group_random.group_random_group_size(lst, group_size)
    actual_output2 = group_random.group_random_group_size(lst2, group_size)

    assert len(actual_output) == 12 // size_count
    assert len(actual_output[0]) == size_count
    assert len(actual_output2) == 6 // size_count
    assert len(actual_output2[0]) == size_count


def test_group_random_extra():
    """Testing the random type of grouping with a group of extra people not assigned
     to their own group"""
    responses = [
        ["Nick", True, False, True, False],
        ["Marvin", False, False, True, True],
        ["Evin", True, True, True, False],
        ["Nikki", True, True, False, False],
        ["Dan", False, True, False, True],
    ]
    grpsize = 2
    num_group = 2
    returned_groups = group_random.group_random_group_size(responses, grpsize)
    returned_groups1 = group_random.group_random_num_group(responses, num_group)
    assert len(returned_groups) == 2
    assert grpsize == 2
    assert len(returned_groups1) == 2
    assert num_group == 2


@given(grpsize=integers(min_value=1, max_value=3))
@settings(verbosity=Verbosity.verbose)
@pytest.mark.hypothesisworks
def test_group_random2(grpsize):
    """This hypothesis test will test the group_random_group_size method"""
    responses = [
        ["Nick", True, False, True, False],
        ["Marvin", False, False, True, True],
        ["Evin", True, True, True, False],
        ["Nikki", True, True, False, False],
        ["Nick", True, False, True, False],
        ["Dan", False, True, False, True],
    ]
    returned_groups = group_random.group_random_group_size(responses, grpsize)
    size_count = grpsize
    assert len(returned_groups[0]) == size_count


def test_group_random():
    """Testing the random type of grouping with everyone in an assigned group"""
    responses = [
        ["Nick", True, False, True, False],
        ["Marvin", False, False, True, True],
        ["Evin", True, True, True, False],
        ["Nikki", True, True, False, False],
        ["Dan", False, True, False, True],
        ["Michael", True, True, False, False],
    ]
    grpsize = 2
    num_group = 3
    returned_groups = group_random.group_random_group_size(responses, grpsize)
    returned_groups1 = group_random.group_random_num_group(responses, num_group)
    assert len(returned_groups) == 3
    assert len(returned_groups1[0]) == 2


def test_shuffle():
    """Checking the shuffle_students method for appropriate ouput"""
    student_identifiers = [
        "Dan",
        "Nikki",
        "Nick",
        "Jeff",
        "Austin",
        "Simon",
        "Jesse",
        "Maria",
    ]
    shuffled_students = group_random.shuffle_students(student_identifiers)
    for i in range(0, len(shuffled_students)):
        assert student_identifiers[i] in shuffled_students
    assert student_identifiers != shuffled_students


def test_round_robin():
    """Testing the round robin function to assure proper output"""
    lst = [
        ["Dan", True, True, True],
        ["Jesse", True, True, True],
        ["Austin", True, True, True],
        ["Nick", False, False, False],
        ["Nikki", False, False, False],
        ["Maria", False, False, False],
        ["Jeff", False, False, False],
        ["Simon", False, False, False],
        ["Jon", False, False, False],
        ["Angie", False, False, False],
        ["Izaak", False, False, False],
        ["Jacob", False, False, False],
    ]
    group_size = 3
    actual_output = group_rrobin.group_rrobin_group_size(lst, group_size)
    assert len(actual_output) == 4
    assert len(actual_output[0]) == group_size
    assert ["Dan", True, True, True] in actual_output[0]
    assert ["Jesse", True, True, True] in actual_output[2]
    assert ["Austin", True, True, True] in actual_output[1]


def test_rrobin_responses():
    """Testing the grouping function according to responses"""
    lst = [
        ["Dan", True, True, True],
        ["Jesse", True, True, True],
        ["Austin", True, True, True],
        ["Nick", False, False, False],
        ["Nikki", False, False, False],
        ["Maria", False, False, False],
        ["Jeff", False, False, False],
        ["Simon", False, False, False],
        ["Jon", False, False, False],
        ["Angie", False, False, False],
        ["Izaak", False, False, False],
        ["Jacob", False, False, False],
    ]
    numgrps = 4
    response_output = group_rrobin.group_rrobin_num_group(lst, numgrps)
    assert len(response_output[0]) == 3
    assert len(response_output) == numgrps
    assert ["Dan", True, True, True] in response_output[0]
    assert ["Jesse", True, True, True] in response_output[2]
    assert ["Austin", True, True, True] in response_output[1]


def test_random():
    """Testing the random grouping function to assure proper output"""
    lst = [
        ["Dan", True, True, True],
        ["Jesse", True, True, True],
        ["Austin", True, True, True],
        ["Nick", False, False, False],
        ["Nikki", False, False, False],
        ["Maria", False, False, False],
        ["Jeff", False, False, False],
        ["Simon", False, False, False],
        ["Jon", False, False, False],
        ["Angie", False, False, False],
        ["Izaak", False, False, False],
        ["Jacob", False, False, False],
    ]
    group_size = 4
    num_group = 3
    actual_output = group_random.group_random_group_size(lst, group_size)
    actual_output1 = group_random.group_random_num_group(lst, num_group)
    assert len(actual_output) == 3
    assert len(actual_output[0]) == 4
    assert len(actual_output1) == 3
    assert len(actual_output1[0]) == 4
