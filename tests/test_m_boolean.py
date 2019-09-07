from io import StringIO
import sys
from clinput.multi import boolean


class TestBoolean:
    """Unit tests for the boolean function for multiple user input."""
    def test_one(self):
        """Test an input of 1."""
        sys.stdin = StringIO("1")
        sys.stdout = StringIO()
        value = boolean("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [True]
        for val in value:
            assert type(val) is bool

    def test_zero(self):
        """Test an input of 0."""
        sys.stdin = StringIO("0")
        sys.stdout = StringIO()
        value = boolean("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [False]
        for val in value:
            assert type(val) is bool

    def test_blank(self):
        """Test a blank input."""
        sys.stdin = StringIO("\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = boolean("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: Please provide an input."
                                         "\nEnter: ")
        assert value == [True]
        for val in value:
            assert type(val) is bool

    def test_string(self):
        """Test a non-boolean string in a list of 1s and 0s."""
        sys.stdin = StringIO("1 0 spam 1\n1")  # last input 1 to break loop
        sys.stdout = StringIO()
        value = boolean("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"spam\"\n"
                                         "Please only enter 1s (True) or "
                                         "0s (False)."
                                         "\nEnter: ")
        assert value == [True]
        for val in value:
            assert type(val) is bool

    def test_many_bool(self):
        """Test a few 1s and 0s in a row."""
        sys.stdin = StringIO("1 0 1 1 0")
        sys.stdout = StringIO()
        value = boolean("Enter: ")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [True, False, True, True, False]
        for val in value:
            assert type(val) is bool

    def test_multi_error(self):
        """Test multiple errors in a row."""
        sys.stdin = StringIO("spam\nham\neggs\n1")
        sys.stdout = StringIO()
        value = boolean("Enter: ")
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"spam\"\n"
                                         "Please only enter 1s (True) or "
                                         "0s (False)."
                                         "\nEnter: "
                                         "Failed on item: \"ham\"\n"
                                         "Please only enter 1s (True) or "
                                         "0s (False)."
                                         "\nEnter: "
                                         "Failed on item: \"eggs\"\n"
                                         "Please only enter 1s (True) or "
                                         "0s (False)."
                                         "\nEnter: ")
        assert value == [True]
        for val in value:
            assert type(val) is bool

    def test_custom_msg(self):
        """Test custom error message."""
        sys.stdin = StringIO("1 spam 1\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = boolean("Enter: ", err="No, not that!")
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"spam\"\n"
                                         "No, not that!\n"
                                         "Enter: ")
        assert value == [True]
        for val in value:
            assert type(val) is bool

    def test_different_sep(self):
        """Test separating character other than sep."""
        sys.stdin = StringIO("1|0|0")
        sys.stdout = StringIO()
        value = boolean("Enter: ", sep="|")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == [True, False, False]
        for val in value:
            assert type(val) is bool
