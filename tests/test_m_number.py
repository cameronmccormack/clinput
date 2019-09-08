from io import StringIO
import sys
from clinput.multi import number


class TestNumber:
    """Unit tests for the number function for multiple user input."""
    def test_one(self):
        """Test an input of 1."""
        sys.stdin = StringIO("1")
        sys.stdout = StringIO()
        value = number("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [1]
        for val in value:
            assert type(val) is float

    def test_zero(self):
        """Test an input of 0."""
        sys.stdin = StringIO("0\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = number("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [0]
        for val in value:
            assert type(val) is float

    def test_blank(self):
        """Test a blank input."""
        sys.stdin = StringIO("\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = number("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please provide an input."
                                         "\nEnter: ")
        assert value == [1]
        for val in value:
            assert type(val) is float

    def test_big(self):
        """Test some really big numbers."""
        sys.stdin = StringIO("83501385134135.3317591735386482 9318512148 "
                             "124871551349.2 129441")
        sys.stdout = StringIO()
        value = number("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [83501385134135.3317591735386482,
                         9318512148,
                         124871551349.2,
                         129441]
        for val in value:
            assert type(val) is float

    def test_negative(self):
        """Test a negative number in a list of positive numbers."""
        sys.stdin = StringIO("13.5 -43.4 34.3 2.2 3.1")
        sys.stdout = StringIO()
        value = number("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [13.5, -43.4, 34.3, 2.2, 3.1]
        for val in value:
            assert type(val) is float

    def test_string(self):
        """Test a non-number string in a list of positive numbers."""
        sys.stdin = StringIO("151 241 spam 1\n1")  # last input 1 to break loop
        sys.stdout = StringIO()
        value = number("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"spam\"\n"
                                         "Please only enter numbers."
                                         "\nEnter: ")
        assert value == [1]
        for val in value:
            assert type(val) is float

    def test_float(self):
        """Test a non-integer positive number in a list of integers."""
        sys.stdin = StringIO("24 1 4.6 13 1")
        sys.stdout = StringIO()
        value = number("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [24, 1, 4.6, 13, 1]
        for val in value:
            assert type(val) is float

    def test_round_float(self):
        """Test a floating point whole number (this should not be accepted)."""
        sys.stdin = StringIO("14 2 41 2.0 24")
        sys.stdout = StringIO()
        value = number("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [14, 2, 41, 2, 24]
        for val in value:
            assert type(val) is float

    def test_multi_error(self):
        """Test multiple errors in a row."""
        sys.stdin = StringIO("spam\nham\neggs\n1")
        sys.stdout = StringIO()
        value = number("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"spam\"\n"
                                         "Please only enter numbers."
                                         "\nEnter: "
                                         "Failed on item: \"ham\"\n"
                                         "Please only enter numbers."
                                         "\nEnter: "
                                         "Failed on item: \"eggs\"\n"
                                         "Please only enter numbers."
                                         "\nEnter: ")
        assert value == [1]
        for val in value:
            assert type(val) is float

    def test_custom_msg(self):
        """Test custom error message."""
        sys.stdin = StringIO("2 spam 2\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = number("Enter: ", err="No, not that!")
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"spam\"\n"
                                         "No, not that!\n"
                                         "Enter: ")
        assert value == [1]
        for val in value:
            assert type(val) is float

    def test_different_sep(self):
        """Test separating character other than sep."""
        sys.stdin = StringIO("1|2|3|4")
        sys.stdout = StringIO()
        value = number("Enter: ", sep="|")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [1, 2, 3, 4]
        for val in value:
            assert type(val) is float

    def test_spaces(self):
        """Test valid inputs with extra spaces."""
        sys.stdin = StringIO("  1   2  3     4  ")
        sys.stdout = StringIO()
        value = number("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [1, 2, 3, 4]
        for val in value:
            assert type(val) is float

    def test_spaces_sep(self):
        """Test valid inputs with extra spaces and custom sep character."""
        sys.stdin = StringIO("  1 ,  2,  3 ,    4  ")
        sys.stdout = StringIO()
        value = number("Enter: ", sep=",")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [1, 2, 3, 4]
        for val in value:
            assert type(val) is float
