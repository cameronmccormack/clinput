from io import StringIO
import sys
from clinput.single import integer


class TestNatural:
    """Unit tests for the integer function for single user input."""
    def test_one(self):
        """Test an input of 1."""
        sys.stdin = StringIO("1")
        sys.stdout = StringIO()
        value = integer("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == 1

    def test_zero(self):
        """Test an input of 0."""
        sys.stdin = StringIO("0")
        sys.stdout = StringIO()
        value = integer("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == 0

    def test_blank(self):
        """Test a blank input."""
        sys.stdin = StringIO("\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = integer("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please provide an input."
                                         "\nEnter: ")
        assert value == 1

    def test_big(self):
        """Test a really big number."""
        sys.stdin = StringIO("835013851341353317591735386482")
        sys.stdout = StringIO()
        value = integer("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == 835013851341353317591735386482

    def test_negative(self):
        """Test a negative integer."""
        sys.stdin = StringIO("-43")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = integer("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == -43

    def test_string(self):
        """Test a non-number string."""
        sys.stdin = StringIO("spam\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = integer("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please enter an integer."
                                         "\nEnter: ")
        assert value == 1

    def test_float(self):
        """Test a non-integer positive number."""
        sys.stdin = StringIO("4.6\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = integer("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please enter an integer."
                                         "\nEnter: ")
        assert value == 1

    def test_round_float(self):
        """Test a floating point whole number (this should not be accepted)."""
        sys.stdin = StringIO("2.0\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = integer("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please enter an integer."
                                         "\nEnter: ")
        assert value == 1

    def test_multi_error(self):
        """Test multiple errors in a row."""
        sys.stdin = StringIO("spam\nham\neggs\n1")
        sys.stdout = StringIO()
        value = integer("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please enter an integer.\n"
                                         "Enter: Please enter an integer.\n"
                                         "Enter: Please enter an integer.\n"
                                         "Enter: ")
        assert value == 1

    def test_custom_msg(self):
        """Test custom error message."""
        sys.stdin = StringIO("spam\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = integer("Enter: ", err="No, not that!")
        assert sys.stdout.getvalue() == "Enter: No, not that!\nEnter: "
        assert value == 1
