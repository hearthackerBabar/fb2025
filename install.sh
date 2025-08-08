#!/bin/bash

# Facebook Login Tool - Termux Installation Script
# This script will set up the tool on Termux

echo "🔵 Facebook Login Tool - Termux Installer"
echo "=========================================="
echo ""

# Check if we're running on Termux
if [ ! -d "/data/data/com.termux" ]; then
    echo "⚠️  Warning: This script is designed for Termux environment"
    echo "   It may work on other Linux systems but is optimized for Android Termux"
    echo ""
fi

# Update packages
echo "📦 Updating packages..."
if command -v pkg >/dev/null 2>&1; then
    pkg update -y && pkg upgrade -y
elif command -v apt >/dev/null 2>&1; then
    apt update && apt upgrade -y
fi

# Install Python if not present
echo "🐍 Installing Python..."
if command -v pkg >/dev/null 2>&1; then
    pkg install python -y
elif command -v apt >/dev/null 2>&1; then
    apt install python3 python3-pip -y
fi

# Install pip if not present
echo "📋 Installing pip..."
if command -v pkg >/dev/null 2>&1; then
    pkg install python-pip -y
fi

# Install required Python packages
echo "📚 Installing Python dependencies..."
pip install -r requirements.txt

# Make the script executable
chmod +x fb_login_tool.py

echo ""
echo "✅ Installation completed successfully!"
echo ""
echo "🚀 To run the tool:"
echo "   python fb_login_tool.py"
echo ""
echo "📖 For more information, check README.md"
echo ""
