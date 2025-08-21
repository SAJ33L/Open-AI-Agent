import asyncio
from app.time_tracker_agent import agent   # only agent
from agents import Runner

async def main():
    result = await Runner.run(
        agent,
        "Find missing time entries for employee 1 between 2025-08-15 and 2025-08-20."
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
