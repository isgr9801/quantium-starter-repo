#!/bin/bash
set -e
VENV_DIR="./venv"

# Check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Error: Virtual environment directory '$VENV_DIR' not found."
    exit 1
fi

# Activate the virtual environment
source "$VENV_DIR/Scripts/activate"

# Run the test suite with pytest
echo "Running test suite..."
pytest test_task5.py -v

# Capture pytest exit code
TEST_EXIT_CODE=$?

# Check if tests passed
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "All tests passed successfully."
    exit 0