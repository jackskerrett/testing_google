from pytest import mark
from src.app import adder

@mark.parametrize("n1,n2,answer", [
    (3, 4, 7),
    (6, -1, 5),
    (1999, 541, 2540)])

def test_adder(n1, n2, answer):
    assert adder(n1, n2) == answer


nxghmn
