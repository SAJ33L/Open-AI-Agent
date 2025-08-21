# Time Tracker Agent

A minimal example agent that finds missing time entries for an employee between two dates. The agent uses the `openai-agents` framework and a small tool function that returns JSON containing missing dates.

This repository contains a lightweight demo suitable for local development and experimentation.

## Project layout

- `main.py` - entrypoint that runs the agent and prints the final output.
- `app/time_tracker_agent.py` - agent definition and the `find_missing_time_entries` tool (hardcoded sample data).
- `requirements.txt` - Python dependencies used for the project.
- `.env` (optional) - local environment variables (gitignored).

## Requirements

- Python 3.12 (project was tested with a venv created for this workspace)
- A virtual environment (recommended)

Dependencies are listed in `requirements.txt`. Install them into your active environment:

```powershell
# From the project root (Windows PowerShell)
python -m pip install -r requirements.txt
```

## Configuration / API keys

This project can work with either:

- An OpenAI-compatible key exposed as `OPENAI_API_KEY`, or
- A Gemini key exposed as `GEMINI_API_KEY`.

The code reads environment variables (and `.env` if present) via `python-dotenv`.

- To use Gemini (recommended for Google Gemini): set `GEMINI_API_KEY` in your `.env` or environment.
- To use OpenAI, set `OPENAI_API_KEY`.

If both are present, `GEMINI_API_KEY` will be preferred by the Gemini client. The repository's agent code may also mirror one key to the other for compatibility with libraries that expect `OPENAI_API_KEY`.

Example `.env` (do NOT commit this file):

```
GEMINI_API_KEY=your_gemini_api_key_here
# or
OPENAI_API_KEY=your_openai_api_key_here
```

Add `.env` to `.gitignore` (already present in this repo) to avoid committing secrets.

## Running locally

1. Create and activate a virtual environment (optional, but recommended):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

3. Ensure you have an API key in your environment or in `.env`.

4. Run the agent:

```powershell
python main.py
```

The script will call the agent with a sample prompt and print the agent's final output.

## Files you may want to edit

- `app/time_tracker_agent.py`: replace the hardcoded sample data with your data source, add or modify tools, or change agent instructions and model name.
- `main.py`: change the prompt or hook the agent into a different interface.

## Security notes

- Never commit API keys or `.env` files to source control.
- Use platform-managed secrets (CI/CD secret stores, cloud secret managers) for production deployments.

## Next steps / improvements

- Add unit tests for `find_missing_time_entries`.
- Replace hardcoded data with a small SQLite or JSON-backed datastore.
- Add a small CLI or FastAPI wrapper for interactive use.

If you'd like, I can wire GEMINI/OPENAI key loading logic into the agent automatically or add a small CLI wrapper—tell me which and I will implement it.
