import pytest
def fun3(x):
    print("Kolejna Funkcja")
    return x-4
def test():
    assert fun3(11) == 7