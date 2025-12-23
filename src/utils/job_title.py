
JOB_GROUPS = {
    "SOFTWARE_ENGINEER": ["software", "developer", "programmer","máy tính", "phần mềm", "angular", "front-end",
                          "backend", "frontend", "fullstack", "web developer", ".net", "dotnet", "web", "php", "nodejs", "java"],
    "MOBILE_DEVELOPER": ["android", "ios", "mobile", "flutter", "react native"],
    "DATA_ENGINEER": ["data engineer", "big data", "etl"],
    "DATA_ANALYST": ["data analyst", "business intelligence", "bi"],
    "AI_ENGINEER": ["ai engineer", "machine learning", "computer vision", "nlp"],
    "QA_TESTER": ["qa", "qc", "tester", "test engineer","test"],
    "DEVOPS_ENGINEER": ["devops", "sre", "cloud engineer", "infra"],
    "BUSINESS_ANALYST": ["business analyst", "ba", "phân tích nghiệp vụ"],
    "PROJECT_MANAGER": ["project manager", "scrum master", "delivery manager"],
    "IT_SUPPORT": ["it support", "helpdesk", "support",],
    "UI_UX_DESIGNER": ["ui", "ux", "designer", "web designer"],
    "MARKETING":["marketing"],
    "PRODUCT OWNER":["product owner", "quản lý dự án"]
}

LEVEL_KEYWORDS = {
    "INTERN": ["intern", "thực tập", "thực tập sinh"],
    "FRESHER": ["fresher", "không yêu cầu kinh nghiệm", "chưa cần kinh nghiệm", "mới ra trường"],
    "JUNIOR": ["junior", "jr", "dưới 1 năm", "1 năm kinh nghiệm"],
    "MIDDLE": ["middle", "mid", "2 năm kinh nghiệm", "3 năm kinh nghiệm", "2+ năm", "3+ năm"],
    "SENIOR": ["senior", "sr", "4 năm kinh nghiệm", "5 năm kinh nghiệm", "4+ năm", "5+ năm", "trên 3 năm"],
    "LEAD": ["lead", "tech lead", "team lead", "trưởng nhóm"],
    "MANAGER": ["manager", "quản lý", "trưởng phòng", "head"]
}

LEVEL_PRIORITY = ["MANAGER", "LEAD", "SENIOR", "MIDDLE", "JUNIOR", "FRESHER", "INTERN"]

def get_position(title):
    title = title.lower()
    
    for group, keywords in JOB_GROUPS.items():
        for kw in keywords:
            if kw in title:
                return group

    return "OTHER"

def get_level(job_title: str) -> str:
    text = job_title.lower()

    for level in LEVEL_PRIORITY:
        for keyword in LEVEL_KEYWORDS[level]:
            if keyword in text:
                return level

    return "UNKNOWN"
