import asyncio
from app.time_tracker_agent import agent as time_tracker_agent
from app.terminal_email_agent import agent as email_agent
from agents import Runner

async def main():
    # Run time tracker agent
    print("Running Time Tracker Agent...")
    time_result = await Runner.run(
        time_tracker_agent,
        "Find missing time entries for employee 1 between 2025-08-15 and 2025-08-20."
    )
    
    print("Time Tracker Response:")
    print(time_result.final_output)
    print("\n" + "="*50 + "\n")
    
    # Run email agent with time tracker response
    print("Running Terminal Email Agent...")
    email_result = await Runner.run(
        email_agent,
        f"Send email notifications for this missing time data: {time_result.final_output}"
    )
    
    print("Email Agent Response:")
    print(email_result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
