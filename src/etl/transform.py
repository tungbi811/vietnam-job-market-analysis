import ftfy
import pandas as pd
from utils.salary import get_min_salary, get_max_salary
from utils.job_title import get_position, get_level
from utils.address import CITIES

def clean_vietnamese_text(text):
    return ftfy.fix_text(text)

def transform(df):
    for col in df.columns:
        df[col] = df[col].apply(clean_vietnamese_text)

    df["min_salary"] = df["salary"].apply(get_min_salary)
    df["max_salary"] = df["salary"].apply(get_max_salary)
    df["salary_unit"] = df["salary"].apply(
        lambda s : "million VND" if "triệu" in s else ("USD" if "USD" in s else "negotiate") 
    )
    df["position"] = df["job_title"].apply(get_position)
    df["level"] = df["job_title"].apply(get_level)
    df["address"] = df["address"].replace(
        {
            "HÃ  Ná»™i": "Hà Nội",
            "Nước Ngoà i": "Nước Ngoài",
            "Toà n Quốc": "Toàn Quốc",
        }
    )
    rows = []
    for _, row in df.iterrows():
        parts = row["address"].split(":")
        for i in range(len(parts)):
            if parts[i] in CITIES:
                if i < len(parts) - 1:
                    if parts[i+1] not in CITIES:
                        row["city"] = parts[i]
                        row["district"] = parts[i+1]
                    else:
                        row["city"] = parts[i]
                        row["district"] = ""
                else:
                    row["city"] = parts[i]
                    row["district"] = ""
                rows.append(row)
    cleaned_df = pd.DataFrame(rows)
    return cleaned_df