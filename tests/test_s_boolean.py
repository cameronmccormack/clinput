from io import StringIO
import sys
from clinput.single import boolean


class TestBoolean:
    """Unit tests for the boolean function for single user input."""
    def test_one(self):
        """Test an input of 1."""
        sys.stdin = StringIO("1")
        sys.stdout = StringIO()
        value = boolean("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value is True
        assert type(value) is bool

    def test_zero(self):
        """Test an input of 0."""
        sys.stdin = StringIO("0")
        sys.stdout = StringIO()
        value = boolean("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value is False
        assert type(value) is bool

    def test_blank(self):
        """Test a blank input."""
        sys.stdin = StringIO("\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = boolean("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please provide an input.\n"
                                         "Enter: ")
        assert value is True
        assert type(value) is bool

    def test_string(self):
        """Test a non-number string."""
        sys.stdin = StringIO("spam\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = boolean("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please enter 1 (True) or 0 "
                                         "(False).\nEnter: ")
        assert value is True
        assert type(value) is bool

    def test_float_positive(self):
        """Test a non-integer positive number."""
        sys.stdin = StringIO("4.6\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = boolean("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please enter 1 (True) or 0 "
                                         "(False).\nEnter: ")
        assert value is True
        assert type(value) is bool

    def test_multi_error(self):
        """Test multiple errors in a row."""
        sys.stdin = StringIO("spam\nham\neggs\n1")
        sys.stdout = StringIO()
        value = boolean("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please enter 1 (True) or 0 "
                                         "(False).\n"
                                         "Enter: Please enter 1 (True) or 0 "
                                         "(False).\n"
                                         "Enter: Please enter 1 (True) or 0 "
                                         "(False).\n"
                                         "Enter: ")
        assert value is True
        assert type(value) is bool

    def test_custom_msg(self):
        """Test custom error message."""
        sys.stdin = StringIO("spam\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = boolean("Enter: ", err="No, not that!")
        assert sys.stdout.getvalue() == "Enter: No, not that!\nEnter: "
        assert value is True
        assert type(value) is bool
