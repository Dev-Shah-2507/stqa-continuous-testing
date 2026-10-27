
from student_service import StudentService


def test_get_student_name_valid_id():
    result = StudentService.get_student_name(None, 101)
    assert result == "Aarav Patel"


def test_get_student_name_second_student():
    result = StudentService.get_student_name(None, 102)
    assert result == "Diya Shah"


def test_get_student_name_invalid_id():
    result = StudentService.get_student_name(None, 999)
    assert result == "Student not found"


def test_get_student_details_valid_id():
    result = StudentService.get_student(None, 101)

    assert "ID: 101" in result
    assert "Name: Aarav Patel" in result
    assert "Course: B.Tech CSE" in result
    assert "Semester: 4" in result


def test_get_student_details_second_student():
    result = StudentService.get_student(None, 103)

    assert "Name: Rohan Mehta" in result
    assert "Course: B.Tech CSE" in result
    assert "Semester: 6" in result


def test_get_student_details_invalid_id():
    result = StudentService.get_student(None, 999)
    assert result == "Student not found"


def test_student_name_returns_string():
    result = StudentService.get_student_name(None, 101)
    assert isinstance(result, str)


def test_student_details_returns_string():
    result = StudentService.get_student(None, 101)
    assert isinstance(result, str)
