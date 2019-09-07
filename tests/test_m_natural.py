from io import StringIO
import sys
from clinput.multi import natural


class TestNatural:
    """Unit tests for the natural number function for multiple user input."""
    def test_one_false(self):
        """Test an input of 1 for natural numbers greater than zero."""
        sys.stdin = StringIO("1")
        sys.stdout = StringIO()
        value = natural("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [1]
        for val in value:
            assert type(val) is int

    def test_one_true(self):
        """Test an input of 1 for natural numbers greater than or equal to
        zero.
        """
        sys.stdin = StringIO("1")
        sys.stdout = StringIO()
        value = natural("Enter: ", zero=True)
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [1]
        for val in value:
            assert type(val) is int

    def test_zero_false(self):
        """Test an input of 0 for natural numbers greater than zero."""
        sys.stdin = StringIO("0\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = natural("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"0\"\n"
                                         "Please only enter positive integers."
                                         "\nEnter: ")
        assert value == [1]
        for val in value:
            assert type(val) is int

    def test_zero_true(self):
        """Test an input of 1 for natural numbers greater than or equal to
        zero.
        """
        sys.stdin = StringIO("0\n1")  # last input 1 shouldn't be reached
        sys.stdout = StringIO()
        value = natural("Enter: ", zero=True)
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [0]
        for val in value:
            assert type(val) is int

    def test_blank(self):
        """Test a blank input."""
        sys.stdin = StringIO("\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = natural("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please provide an input."
                                         "\nEnter: ")
        assert value == [1]
        for val in value:
            assert type(val) is int

    def test_big(self):
        """Test some really big numbers."""
        sys.stdin = StringIO("835013851341353317591735386482 9318512148 "
                             "1248715513492 129441")
        sys.stdout = StringIO()
        value = natural("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [835013851341353317591735386482,
                         9318512148,
                         1248715513492,
                         129441]
        for val in value:
            assert type(val) is int

    def test_negative(self):
        """Test a negative integer in a list of positive integers."""
        sys.stdin = StringIO("13 -43 34 2 3\n1")  # last input 1 to break loop
        sys.stdout = StringIO()
        value = natural("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"-43\"\n"
                                         "Please only enter positive integers."
                                         "\nEnter: ")
        assert value == [1]
        for val in value:
            assert type(val) is int

    def test_string(self):
        """Test a non-number string in a list of positive integers."""
        sys.stdin = StringIO("151 241 spam 1\n1")  # last input 1 to break loop
        sys.stdout = StringIO()
        value = natural("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"spam\"\n"
                                         "Please only enter positive integers."
                                         "\nEnter: ")
        assert value == [1]
        for val in value:
            assert type(val) is int

    def test_float(self):
        """Test a non-integer positive number in a list of integers."""
        sys.stdin = StringIO("24 1 4.6 13 1\n1")  # last input 1 to break loop
        sys.stdout = StringIO()
        value = natural("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"4.6\"\n"
                                         "Please only enter positive integers."
                                         "\nEnter: ")
        assert value == [1]
        for val in value:
            assert type(val) is int

    def test_round_float(self):
        """Test a floating point whole number (this should not be accepted)."""
        sys.stdin = StringIO("14 2 41 2.0 24\n1")  # last input 1 to break loop
        sys.stdout = StringIO()
        value = natural("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"2.0\"\n"
                                         "Please only enter positive integers."
                                         "\nEnter: ")
        assert value == [1]
        for val in value:
            assert type(val) is int

    def test_multi_error(self):
        """Test multiple errors in a row."""
        sys.stdin = StringIO("spam\nham\neggs\n1")
        sys.stdout = StringIO()
        value = natural("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"spam\"\n"
                                         "Please only enter positive integers."
                                         "\nEnter: "
                                         "Failed on item: \"ham\"\n"
                                         "Please only enter positive integers."
                                         "\nEnter: "
                                         "Failed on item: \"eggs\"\n"
                                         "Please only enter positive integers."
                                         "\nEnter: ")
        assert value == [1]
        for val in value:
            assert type(val) is int

    def test_custom_msg(self):
        """Test custom error message."""
        sys.stdin = StringIO("2 spam 2\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = natural("Enter: ", err="No, not that!")
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"spam\"\n"
                                         "No, not that!\n"
                                         "Enter: ")
        assert value == [1]
        for val in value:
            assert type(val) is int
