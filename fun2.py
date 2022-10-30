import pytest
def fun2(x):
    print("Funkcja")
    return x*3
def test():
    assert fun2(5) == 15
