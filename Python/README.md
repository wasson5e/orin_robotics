# Python Automation

## Google script for multiple VENV
```
import subprocess
import sys
import os

def run_script_in_env(env_path, script_path, *args):
    """
    Runs a Python script using a specific virtual environment's interpreter.

    :param env_path: Path to the root directory of the virtual environment (e.g., "./other_venv").
    :param script_path: Path to the script to run.
    :param args: Command line arguments for the script.
    :return: The stdout from the script as a string.
    """
    # Determine the correct Python executable path based on OS
    if os.name == 'nt':  # Windows
        python_executable = os.path.join(env_path, 'Scripts', 'python.exe')
    else:  # Unix/macOS
        python_executable = os.path.join(env_path, 'bin', 'python')

    if not os.path.exists(python_executable):
        print(f"Error: Python executable not found at {python_executable}")
        sys.exit(1)

    # Build the command list: [interpreter_path, script_path, arg1, arg2, ...]
    command = [python_executable, script_path] + list(args)

    # Run the subprocess
    # capture_output=True captures stdout and stderr
    # text=True decodes the output to strings
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Subprocess failed: {e.stderr}")
        sys.exit(1)

# --- Example Usage ---
# Define paths relative to your main script's location
venv_dir = "./other_venv"
target_script = "other_env_script.py"

# Example arguments to pass to the target script
arguments = ["--user", "data_file.txt"]

output = run_script_in_env(venv_dir, target_script, *arguments)
print(f"Output from other script:\n{output}")

```