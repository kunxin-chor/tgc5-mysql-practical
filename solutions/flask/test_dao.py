import data
import pytest

def test_get_employees():
    employees = data.get_employees()
    assert employees.rowcount == 8