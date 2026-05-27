#!/bin/bash
# Install dependencies (Linux)
sudo apt-get update && sudo apt-get install -y xclip

# Create virtual environment
python3 -m venv venv
source venv/bin/activate
pip install pyperclip pynput

# Run tests
echo "Running tests..."
python3 -m unittest test_unformat_paste.py

# Start daemon
echo "Starting daemon..."
python3 main.py start