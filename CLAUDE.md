# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a learning project for experimenting with the Gemini API. The project is set up as a Python package using `uv` for dependency management and is designed to run in a devcontainer environment.

## Development Environment

- **Python Version**: 3.14
- **Package Manager**: `uv` (replaces pip/poetry)
- **Container**: Devcontainer configured with VS Code extensions for Claude Code, Gemini CLI, and ChatGPT
- **Timezone**: Asia/Tokyo

## Common Commands

### Environment Setup
```bash
# Install dependencies (uv reads from pyproject.toml)
uv sync

# Add a new dependency
uv add <package-name>

# Add a dev dependency
uv add --dev <package-name>
```

### Running the Project
```bash
# Run the main script
python main.py

# Or using uv
uv run main.py
```

### Environment Variables
- Environment variables are loaded from `.env` file (configured via `UV_ENV_FILE=.env`)
- Do not commit `.env` to version control

## Project Structure

This is currently a simple single-file project with `main.py` as the entry point. The project uses:
- `uv` for dependency management and virtual environment handling
- Devcontainer setup with multiple AI coding assistants (Claude Code, Gemini CLI, ChatGPT)
- Configuration volumes for persistent AI assistant settings

## Key Configuration Files

- `pyproject.toml`: Project metadata and dependencies
- `.env`: Environment variables (not committed to git)
- `.devcontainer/devcontainer.json`: Devcontainer configuration with AI assistant extensions
- `.devcontainer/post-start.sh`: Post-start script for fixing permissions on AI config directories
