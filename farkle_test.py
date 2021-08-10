#!python3

from farkle import *


def test_check_three_pair():
    assert check_three_pair([1, 1, 3, 3, 5, 5]) == 1500

def test_check_four_two():
    assert check_four_two([1, 1, 1, 1, 5, 5]) == 1500

def test_check_set_of_six():
    assert check_set_of_six([1, 1, 1, 1, 1, 1]) == 3000

def test_check_set_of_five():
    assert check_set_of_five([1, 1, 1, 1, 1]) == 2000

def test_check_set_of_four():
    assert check_set_of_four([1, 1, 1, 1]) == 1000

def test_check_three_triplets():
    assert check_three_triplets([1, 1, 1, 5, 5, 5]) == 2500

def test_check_straight():
    assert check_straight([1, 2, 3, 4, 5, 6]) == 1500

def test_six_triple():
    assert check_triple([6,6,6,3,2,1]) == 600

def test_five_triple():
    assert check_triple([5,5,5,3,2,1]) == 500

def test_four_triple():
    assert check_triple([4,4,4,3,2,1]) == 400
    
def test_three_triple():
    assert check_triple([3,3,3,1,2,1]) == 300

def test_two_triple():
    assert check_triple([2,2,2,3,1,5]) == 200

def test_one_triple():
    assert check_triple([1,1,1,2,3,5]) == 100

def test_check_ones():
    assert check_ones([1,1,4,5,6,3]) == 200

def test_check_fives():
    assert check_fives([1,1,4,5,6,3]) == 50