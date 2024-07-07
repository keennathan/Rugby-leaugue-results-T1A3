#!/bin/bash

# Check if Python 3.10 is installed
if ! python3.10 --version >/dev/null 2>&1; then
    echo "Python 3.10 is not installed. Trying to install..."
    if command -v sudo >/dev/null 2>&1; then
        sudo apt update && sudo apt install -y python3.10
        if [ $? -ne 0 ]; then
            echo "Failed to install Python 3.10. Please install it manually."
            exit 1
        fi
    else
        echo "sudo is not available. Please install Python 3.10 manually."
        exit 1
    fi
fi

# Check if pip is installed
if ! command -v pip >/dev/null 2>&1; then
    echo "pip is not installed. Trying to install..."
    if command -v sudo >/dev/null 2>&1; then
        sudo apt update && sudo apt install -y python3-pip
        if [ $? -ne 0 ]; then
            echo "Failed to install pip. Please install it manually."
            exit 1
        fi
    else
        echo "sudo is not available. Please install pip manually."
        exit 1
    fi
fi

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