import pytest
from student_registry import Student


@pytest.fixture
def student():
    return Student("Alice", 13, "12th", 1)


def test_student_initialization(student):
    assert student.get_name == "Alice"
    assert student.get_age == 13
    assert student.get_grade == "12th"


def test_student_name_setter(student):
    student.set_name = "Alex"
    assert student.get_name == "Alex"


def test_student_age_setter(student):
    student.set_age = 14
    assert student.get_age == 14


def test_student_grade_setter(student):
    student.set_grade = "10th"
    assert student.get_grade == "10th"


def test_invalid_name_setter(student):
    student.set_name = 123
    assert student.get_name == "Alice"


def test_invalid_age_setter(student):
    student.set_age = "invalid"
    assert student.get_age == 13


def test_invalid_grade_setter(student):
    student.set_grade = "13th"
    assert student.get_grade == "12th"


# Write tests for Class methods
def test_study(student):
    assert student.study("Geometry") == f"{student.get_name} is studying Geometry"
    assert student.get_subjects == ["Geometry"]


def test_advance(student):
    student.set_grade = "10th"
    assert student.advance(1) == f"{student.get_name} has advanced to the 11th grade"
    assert student.get_grade == "11th"
