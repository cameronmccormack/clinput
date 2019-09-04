from io import StringIO
import sys
from clinput.single import natural


class TestNatural:
    """Unit tests for the natural number function for single user input."""
    def test_one_false(self):
        """Test an input of 1 for natural numbers greater than zero."""
        sys.stdin = StringIO("1")
        sys.stdout = StringIO()
        value = natural("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == 1

    def test_one_true(self):
        """Test an input of 1 for natural numbers greater than or equal to
        zero.
        """
        sys.stdin = StringIO("1")
        sys.stdout = StringIO()
        value = natural("Enter: ", zero=True)
        assert sys.stdout.getvalue() == "Enter: "
        assert value == 1

    def test_zero_false(self):
        """Test an input of 0 for natural numbers greater than zero."""
        sys.stdin = StringIO("0\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = natural("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please enter an integer "
                                         "greater than zero.\nEnter: ")
        assert value == 1

    def test_zero_true(self):
        """Test an input of 1 for natural numbers greater than or equal to
        zero.
        """
        sys.stdin = StringIO("0\n1")  # last input 1 shouldn't be reached
        sys.stdout = StringIO()
        value = natural("Enter: ", zero=True)
        assert sys.stdout.getvalue() == "Enter: "
        assert value == 0

    def test_blank(self):
        """Test a blank input."""
        sys.stdin = StringIO("\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = natural("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please enter an integer "
                                         "greater than zero.\nEnter: ")
        assert value == 1

    def test_none(self):
        """Test a null input."""
        sys.stdin = StringIO(None)
        sys.stdout = StringIO()
        value = natural("Enter: ")
        assert value = None
