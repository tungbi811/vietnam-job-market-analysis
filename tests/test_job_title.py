from src.utils.job_title import get_level, get_position

def test_position_software_engineer():
    title = "Lập trình viên phần mềm"
    assert get_position(title) == "SOFTWARE_ENGINEER"

def test_position_backend_developer():
    title = "Lập trình viên Backend Java"
    assert get_position(title) == "SOFTWARE_ENGINEER"

def test_position_ai_engineer():
    title = "Kỹ sư AI Machine Learning"
    assert get_position(title) == "AI_ENGINEER"

def test_position_other():
    title = "Nhân viên hành chính văn phòng"
    assert get_position(title) == "OTHER"

def test_level_fresher_vietnamese():
    title = "Lập trình viên mới ra trường"
    assert get_level(title) == "FRESHER"

def test_level_intern_vietnamese():
    title = "Thực tập sinh lập trình"
    assert get_level(title) == "INTERN"
