#!/bin/bash

# Check if python3.10-venv is installed
if ! dpkg -s python3.10-venv >/dev/null 2>&1; then
    echo "python3.10-venv is not installed. Trying to install..."
    if command -v sudo >/dev/null 2>&1; then
        sudo apt update && sudo apt install -y python3.10-venv
        if [ $? -ne 0 ]; then
            echo "Failed to install python3.10-venv. Please install it manually."
            exit 1
        fi
    else
        echo "sudo is not available. Please install python3.10-venv manually."
        exit 1
    fi
fi

# Create a virtual environment
python3 -m venv virtualenv

# Activate the virtual environment
source virtualenv/bin/activate

# Install the dependencies from requirements.txt
pip install -r requirements.txt

# Run the main application
python3 main.py

# Deactivate the virtual environment
deactivate