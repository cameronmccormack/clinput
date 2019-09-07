from io import StringIO
import sys
import pytest
from clinput.multi import custom


@pytest.fixture
def custom_data():
    return ("spam", "ham", "eggs", "1", "2", "3")


class TestCustom:
    """Unit tests for the custom function for multiple user input."""
    def test_one(self, custom_data):
        """Test an input of 1."""
        sys.stdin = StringIO("1")
        sys.stdout = StringIO()
        value = custom("Enter: ", custom_data)
        assert sys.stdout.getvalue() == "Enter: "
        assert value == ["1"]
        for val in value:
            assert type(val) is str

    def test_zero(self, custom_data):
        """Test an input of 0."""
        sys.stdin = StringIO("0\nspam")
        sys.stdout = StringIO()
        value = custom("Enter: ", custom_data)
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"0\"\n"
                                         "Invalid input.\n"
                                         "Enter: ")
        assert value == ["spam"]
        for val in value:
            assert type(val) is str

    def test_blank(self, custom_data):
        """Test a blank input."""
        sys.stdin = StringIO("\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = custom("Enter: ", custom_data)
        assert sys.stdout.getvalue() == ("Enter: Please provide an input."
                                         "\nEnter: ")
        assert value == ["1"]
        for val in value:
            assert type(val) is str

    def test_string(self, custom_data):
        """Test an invalid input in a list of valid inputs."""
        sys.stdin = StringIO("spam ham eggs beans ham\nham")
        sys.stdout = StringIO()
        value = custom("Enter: ", custom_data)
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"beans\"\n"
                                         "Invalid input."
                                         "\nEnter: ")
        assert value == ["ham"]
        for val in value:
            assert type(val) is str

    def test_many(self, custom_data):
        """Test a few valid inputs in a row."""
        sys.stdin = StringIO("1 2 3 spam ham eggs")
        sys.stdout = StringIO()
        value = custom("Enter: ", custom_data)
        assert sys.stdout.getvalue() == "Enter: "
        assert value == ["1", "2", "3", "spam", "ham", "eggs"]
        for val in value:
            assert type(val) is str

    def test_multi_error(self, custom_data):
        """Test multiple errors in a row."""
        sys.stdin = StringIO("7\n8\n9\n1")
        sys.stdout = StringIO()
        value = custom("Enter: ", custom_data)
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"7\"\n"
                                         "Invalid input."
                                         "\nEnter: "
                                         "Failed on item: \"8\"\n"
                                         "Invalid input."
                                         "\nEnter: "
                                         "Failed on item: \"9\"\n"
                                         "Invalid input."
                                         "\nEnter: ")
        assert value == ["1"]
        for val in value:
            assert type(val) is str

    def test_custom_msg(self, custom_data):
        """Test custom error message."""
        sys.stdin = StringIO("1 spam 0\n1")  # last input 1 to break input loop
        sys.stdout = StringIO()
        value = custom("Enter: ", custom_data, err="No, not that!")
        assert sys.stdout.getvalue() == ("Enter: "
                                         "Failed on item: \"0\"\n"
                                         "No, not that!\n"
                                         "Enter: ")
        assert value == ["1"]
        for val in value:
            assert type(val) is str

    def test_different_sep(self, custom_data):
        """Test separating character other than sep."""
        sys.stdin = StringIO("1|2|3")
        sys.stdout = StringIO()
        value = custom("Enter: ", custom_data, sep="|")
        assert sys.stdout.getvalue() == "Enter: "
        assert value == ["1", "2", "3"]
        for val in value:
            assert type(val) is str
