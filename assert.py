# Function to check if a number is even
def is_even(n):
    return n % 2 == 0

# Test cases
def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-1) == False
    assert is_even(100) == True
    assert is_even(101) == False

# Run the test cases
if __name__ == '__main__':
    test_is_even()
    print("All tests passed!")
