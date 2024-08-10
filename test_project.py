import sys
import pytest
import project
from io import StringIO
import os
import csv
from tabulate import tabulate
import pytest
from unittest.mock import patch, MagicMock



def main():
    test_previousAttendance()
    test_deleteChoose()
    test_displayMenu()


def test_previousAttendance(monkeypatch):
    """Test when attendanceFolder does not exist."""
    # Mock os.path.exists
    monkeypatch.setattr(os.path, 'exists', lambda _: False)
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        project.previousAttendance("nonexistent_folder")
        assert "File does not exist" in mock_stdout.getvalue()


def test_deleteChoose():
    """ check if the deleteChose function return None if their is no folder"""
    with patch('builtins.input', return_value="3"):
        assert project.deleteChoose() is None

def test_displayMenu():
    with patch('builtins.input', side_effect=["y", "n"]):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            project.displayMenu()
            assert "Program Exited" in mock_stdout.getvalue()



if __name__ == "__main__":
    main()