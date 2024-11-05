import main

# Testing
# We want to test the add function in main.py
# We will test the function with different inputs
# We will use the assert statement to check if the function returns the expected output
# We will use the pytest library to run the tests
# We will use the pytest-cov library to get code coverage


def test_add():
    assert main.add(2, 3) == 5
    assert main.add(0, 0) == 0
    assert main.add(5, 4) == 8


# Why do we test?
# To make sure our code works as expected
# To catch bugs early
# To make sure our code is reliable
# To make sure our code is maintainable
# To make sure our code is readable
