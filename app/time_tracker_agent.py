from agents import Agent, function_tool, set_default_openai_key
import json, os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

set_default_openai_key(os.getenv("OPENAI_API_KEY"))
# Hardcoded employee time entries
time_entries = [
    {"employee_id": 1, "date": "2025-08-15", "hours": 8},
    {"employee_id": 1, "date": "2025-08-16", "hours": 6},
    {"employee_id": 1, "date": "2025-08-18", "hours": 7},  # 17th missing
    {"employee_id": 1, "date": "2025-08-19", "hours": 8},
]

@function_tool
def find_missing_time_entries(start_date: str, end_date: str, employee_id: int) -> str:
    """
    Find missing dates for a given employee in a date range.
    Returns JSON in format [{empid, missing_date}].
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    logged_dates = {
        datetime.strptime(e["date"], "%Y-%m-%d").date()
        for e in time_entries if e["employee_id"] == employee_id
    }

    missing_entries = []
    current = start
    while current <= end:
        if current.date() not in logged_dates:
            missing_entries.append({
                "empid": employee_id,
                "missing_date": str(current.date())
            })
        current += timedelta(days=1)

    return json.dumps(missing_entries)

# Define agent
agent = Agent(
    name="Time Tracker Agent",
    instructions="You are a time tracking agent. Use the tool to find missing time entries. Return ONLY the raw JSON data without any markdown formatting, code blocks, or additional text. Do not include ```json``` or any other formatting markers.",
    tools=[find_missing_time_entries],
)
