from helpers import press_sequence


def test_sum():
    assert press_sequence('1 + 2 =') == '3'

def test_sub():
    assert press_sequence('5 - 1 5 =') == '-10'

def test_negneg():
    assert press_sequence('- 1 - - 2 =') == '1'
