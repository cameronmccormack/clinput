from io import StringIO
import sys
from clinput.single import string


class TestString:
    """Unit tests for the string function for single user input."""
    def test_one(self):
        """Test an input of 1."""
        sys.stdin = StringIO("1")
        sys.stdout = StringIO()
        value = string("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == "1"
        assert type(value) is str

    def test_zero(self):
        """Test an input of 0."""
        sys.stdin = StringIO("0")
        sys.stdout = StringIO()
        value = string("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == "0"
        assert type(value) is str

    def test_blank(self):
        """Test a blank input."""
        sys.stdin = StringIO("\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = string("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please provide an input.\n"
                                         "Enter: ")
        assert value == "1"
        assert type(value) is str

    def test_string(self):
        """Test a non-number string."""
        sys.stdin = StringIO("spam")
        sys.stdout = StringIO()
        value = string("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == "spam"
        assert type(value) is str

    def test_multi_error(self):
        """Test multiple errors in a row."""
        sys.stdin = StringIO("\n\n\neggs")
        sys.stdout = StringIO()
        value = string("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please provide an input.\n"
                                         "Enter: Please provide an input.\n"
                                         "Enter: Please provide an input.\n"
                                         "Enter: ")
        assert value == "eggs"
        assert type(value) is str

    def test_custom_msg(self):
        """Test custom error message."""
        sys.stdin = StringIO("\nham")
        sys.stdout = StringIO()
        value = string("Enter: ", err="No, not that!")
        assert sys.stdout.getvalue() == "Enter: No, not that!\nEnter: "
        assert value == "ham"
        assert type(value) is str
