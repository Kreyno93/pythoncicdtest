import main


def test_add():
    assert main.add(2, 3) == 5
    assert main.add(0, 0) == 0
    assert main.add(5, 4) == 8
