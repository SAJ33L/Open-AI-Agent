from agents import Agent, function_tool, set_default_openai_key
import json, os
from dotenv import load_dotenv

load_dotenv()

set_default_openai_key(os.getenv("OPENAI_API_KEY"))

@function_tool
def send_email_notification(missing_entries_json: str) -> str:
    """
    Takes JSON response from time tracker and prints email notifications to terminal.
    """
    try:
        # Parse the JSON response
        missing_entries = json.loads(missing_entries_json)
        
        # Group by employee ID
        employee_notifications = {}
        for entry in missing_entries:
            empid = entry["empid"]
            missing_date = entry["missing_date"]
            
            if empid not in employee_notifications:
                employee_notifications[empid] = []
            employee_notifications[empid].append(missing_date)
        
        # Print email notifications for each employee
        for empid, dates in employee_notifications.items():
            print(f"Email sent to employee {empid} about missing hours on dates: {', '.join(dates)}")
        
        return f"Email notifications sent to {len(employee_notifications)} employees"
        
    except json.JSONDecodeError:
        return "Error: Invalid JSON format received"

# Define agent
agent = Agent(
    name="Terminal Email Agent",
    instructions="You are an email notification agent. Take JSON data about missing time entries and send email notifications by printing to terminal.",
    tools=[send_email_notification],
)