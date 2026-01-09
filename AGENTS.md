# Repository Guidelines

## Project Structure & Module Organization
- `main.py` is the single entry point for the Gemini API experiments.
- `pyproject.toml` defines the project metadata and dependencies for `uv`.
- `uv.lock` pins resolved dependencies.
- `.devcontainer/` holds the devcontainer setup for consistent local tooling.
- `.env` is used for local secrets and is not committed.

## Build, Test, and Development Commands
- `uv sync` installs dependencies from `pyproject.toml`.
- `uv add <package>` adds a runtime dependency; `uv add --dev <package>` adds a dev dependency.
- `uv run main.py` runs the app inside the `uv` environment.
- `python main.py` runs directly if your environment already matches `pyproject.toml`.

## Coding Style & Naming Conventions
- Use Python 3.14 features and standard 4-space indentation.
- Keep module/file names lowercase with underscores if new files are added (e.g., `gemini_client.py`).
- Prefer clear, explicit variable names over abbreviations in examples and experiments.

## Testing Guidelines
- No test suite is configured yet. If you add tests, place them in `tests/` and name files `test_*.py`.
- Keep test helpers close to the tests that use them; prefer `pytest` if you introduce a framework.

## Commit & Pull Request Guidelines
- There is no established commit message convention yet; use concise, imperative messages (e.g., "Add Gemini API example").
- PRs should include a short description of changes and any relevant setup notes (e.g., new env vars).

## Security & Configuration Tips
- Store API keys in `.env` and keep them out of version control.
- Document new required environment variables in this file and in `main.py` usage comments.
