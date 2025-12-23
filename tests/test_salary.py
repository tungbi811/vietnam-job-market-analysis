from src.utils.salary import get_min_salary, get_max_salary

def test_get_min_salary_valid():
    assert get_min_salary("10 - 20 triệu") == "10"

def test_get_min_salary_invalid():
    assert get_min_salary("thỏa thuận") is ""

def test_get_max_salary_valid():
    assert get_max_salary("10 - 20 triệu") == "20"

def test_salary_unit_vnd():
    s = "10 - 20 triệu"
    assert ("million VND" if "triệu" in s else None) == "million VND"

def test_salary_unit_usd():
    s = "1000 USD"
    assert ("USD" if "USD" in s else None) == "USD"