import pytest
import io
import sys
from clinput import single


class TestNatural:
    def test_one(self):
        output = io.StringIO()
        sys.stdout = output
        sys.stdin = io.StringIO("1")
        value = single.natural("Enter: ")
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "Enter: "
        assert value == 1

    def test_fail_one(self):
        output = io.StringIO()
        sys.stdout = output
        sys.stdin = io.StringIO("a\n1")
        value = single.natural("Enter: ")
        sys.stdout = sys.__stdout__
        print(output.getvalue())
        assert output.getvalue() == "Enter: Please enter an integer greater than zero.\nEnter: "
        assert value == 1
