from io import StringIO
import sys
from clinput.single import negative


class TestNegative:
    """Unit tests for the negative function for single user input."""
    def test_minus_one_true(self):
        """Test an input of -1 where zero is included."""
        sys.stdin = StringIO("-1")
        sys.stdout = StringIO()
        value = negative("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == -1.0
        assert type(value) is float

    def test_minus_one_false(self):
        """Test an input of -1 where zero is not included."""
        sys.stdin = StringIO("-1")
        sys.stdout = StringIO()
        value = negative("Enter: ", zero=False)
        assert sys.stdout.getvalue() == "Enter: "
        assert value == -1.0
        assert type(value) is float

    def test_zero_true(self):
        """Test an input of 0 where zero is included."""
        sys.stdin = StringIO("0")
        sys.stdout = StringIO()
        value = negative("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == 0.0
        assert type(value) is float

    def test_zero_false(self):
        """Test an input of 0 where zero is not included."""
        sys.stdin = StringIO("0\n-1")  # -1 added to break loop
        sys.stdout = StringIO()
        value = negative("Enter: ", zero=False)
        assert sys.stdout.getvalue() == ("Enter: Please enter a negative "
                                         "number.\nEnter: ")
        assert value == -1.0
        assert type(value) is float

    def test_blank(self):
        """Test a blank input."""
        sys.stdin = StringIO("\n-1")  # last input -1 to break input loop
        sys.stdout = StringIO()
        value = negative("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please provide an input."
                                         "\nEnter: ")
        assert value == -1.0
        assert type(value) is float

    def test_big(self):
        """Test a really big negative number."""
        sys.stdin = StringIO("-835013851341353317591735386482")
        sys.stdout = StringIO()
        value = negative("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == -835013851341353317591735386482.0
        assert type(value) is float

    def test_negative(self):
        """Test a negative integer."""
        sys.stdin = StringIO("-43")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = negative("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == -43.0
        assert type(value) is float

    def test_string(self):
        """Test a non-number string."""
        sys.stdin = StringIO("spam\n-1")  # last input -1 to break input loop
        sys.stdout = StringIO()
        value = negative("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please enter a negative "
                                         "number.\nEnter: ")
        assert value == -1.0
        assert type(value) is float

    def test_float_positive(self):
        """Test a non-integer positive number."""
        sys.stdin = StringIO("4.6\n-1")  # last input -1 to break input loop
        sys.stdout = StringIO()
        value = negative("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please enter a negative "
                                         "number.\nEnter: ")
        assert value == -1.0
        assert type(value) is float

    def test_float_negative(self):
        """Test a non-integer negative number."""
        sys.stdin = StringIO("-87.65")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = negative("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == -87.65
        assert type(value) is float

    def test_round_float(self):
        """Test a floating point whole number."""
        sys.stdin = StringIO("-2.0")
        sys.stdout = StringIO()
        value = negative("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == -2.0
        assert type(value) is float

    def test_multi_error(self):
        """Test multiple errors in a row."""
        sys.stdin = StringIO("spam\nham\neggs\n-1")
        sys.stdout = StringIO()
        value = negative("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please enter a negative "
                                         "number.\n"
                                         "Enter: Please enter a negative "
                                         "number.\n"
                                         "Enter: Please enter a negative "
                                         "number.\n"
                                         "Enter: ")
        assert value == -1.0
        assert type(value) is float

    def test_custom_msg(self):
        """Test custom error message."""
        sys.stdin = StringIO("spam\n-1")  # last input -1 to break input loop
        sys.stdout = StringIO()
        value = negative("Enter: ", err="No, not that!")
        assert sys.stdout.getvalue() == "Enter: No, not that!\nEnter: "
        assert value == -1.0
        assert type(value) is float

    def test_spaces(self):
        """Test whitespace on valid input."""
        sys.stdin = StringIO("  -1   ")
        sys.stdout = StringIO()
        value = negative("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == -1
        assert type(value) is float
