from pytest import mark
from src.app import adder, subber

@mark.parametrize("n1,n2,answer", [
    (3, 4, 7),
    (6, -1, 5),
    (1999, 541, 2540)
])


def test_adder(n1, n2, answer):
    assert adder(n1, n2) == answer

@mark.parametrize("n1,n2,answer",[
    (100,90,10),
    (4,10,-6),
    (5,5,0)
])

def test_subber(n1, n2, answer):
    assert subber(n1, n2) == answer  