# Repository guidance

## Current state

- `main.py` is the current CLI entry point. Keep argument parsing under `if __name__ == '__main__':` and route
  application behavior through `run()` so it remains easy to test.
- `lib.py` defines the `Avatar` type and avatar generation/saving functions. `save_avatar()` is currently a stub that
  raises `NotImplementedError`.
- `tests/` contains the unittest smoke test suite.
- `.venv/` is the local virtual environment; `.idea/` contains PyCharm settings. Avoid changing these unless the task
  specifically requires it.

## Working conventions

- Keep changes focused on the requested task and follow the existing Python style: four-space indentation and
  `snake_case` functions and variables.
- Keep executable startup code under `if __name__ == '__main__':` so importing modules does not run the application.
- Prefer the standard library when practical. When introducing third-party dependencies, add an appropriate dependency
  manifest and document setup and execution.
- Never commit credentials, local environment files, virtual environments, or downloaded model weights. If external
  services are introduced, read credentials from environment variables.
- Document new entry points, configuration, and runtime requirements as the application develops.

## Validation

- Use the local virtual environment's interpreter when the task depends on packages installed there.
- Run the smoke test suite with `.venv/bin/python -m unittest discover`.
