import pytest
from io import StringIO
import sys
from clinput.single import custom


@pytest.fixture
def custom_data():
    return ("spam", "ham", "eggs", "1", "2", "3")


class TestCustom:
    """Unit tests for the custom function for single user input."""
    def test_one(self, custom_data):
        """Test an input of 1."""
        sys.stdin = StringIO("1")
        sys.stdout = StringIO()
        value = custom("Enter: ", custom_data)
        assert sys.stdout.getvalue() == "Enter: "
        assert value == "1"
        assert type(value) is str

    def test_zero(self, custom_data):
        """Test an input of 0."""
        sys.stdin = StringIO("0\n1")
        sys.stdout = StringIO()
        value = custom("Enter: ", custom_data)
        assert sys.stdout.getvalue() == "Enter: Invalid input.\nEnter: "
        assert value == "1"
        assert type(value) is str

    def test_blank(self, custom_data):
        """Test a blank input."""
        sys.stdin = StringIO("\nspam")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = custom("Enter: ", custom_data)
        assert sys.stdout.getvalue() == ("Enter: Please provide an input.\n"
                                         "Enter: ")
        assert value == "spam"
        assert type(value) is str

    def test_string(self, custom_data):
        """Test a non-number string."""
        sys.stdin = StringIO("eggs")
        sys.stdout = StringIO()
        value = custom("Enter: ", custom_data)
        assert sys.stdout.getvalue() == "Enter: "
        assert value == "eggs"
        assert type(value) is str

    def test_multi_error(self, custom_data):
        """Test multiple errors in a row."""
        sys.stdin = StringIO("this\nthat\nthe other\nham")
        sys.stdout = StringIO()
        value = custom("Enter: ", custom_data)
        assert sys.stdout.getvalue() == ("Enter: Invalid input.\n"
                                         "Enter: Invalid input.\n"
                                         "Enter: Invalid input.\n"
                                         "Enter: ")
        assert value == "ham"
        assert type(value) is str

    def test_custom_msg(self, custom_data):
        """Test custom error message."""
        sys.stdin = StringIO("4\n3")
        sys.stdout = StringIO()
        value = custom("Enter: ", custom_data, err="No, not that!")
        assert sys.stdout.getvalue() == "Enter: No, not that!\nEnter: "
        assert value == "3"
        assert type(value) is str
