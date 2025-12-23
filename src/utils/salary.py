import re

def get_min_salary(text):
    numbers = re.findall(r"\d[\d,]*", text)
    if len(numbers) == 2 or "trên" in text.lower():
        return numbers[0]
    elif "thoả thuận" in text.lower():
        return "negotiate"
    else:
        return ""

def get_max_salary(text):
    numbers = re.findall(r"\d[\d,]*", text)
    if len(numbers) == 2:
        return numbers[1]
    elif len(numbers) == 1:
        return numbers[0]
    elif "thoả thuận" in text.lower():
        return "negotiate"
    else:
        return ""
    
