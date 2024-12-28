# add-open-with-VS-Code-to-path---python-method
This repository contains a Python script to add an "Open with VS Code" option to the right-click context menu for files and folders on Windows. With this feature, you can quickly open files or directories in Visual Studio Code directly from Windows Explorer.

# Add 'Open with VS Code' to Context Menu

This repository contains a Python script to add an "Open with VS Code" option to the right-click context menu for files and folders on Windows. With this feature, you can quickly open files or directories in Visual Studio Code directly from Windows Explorer.

## Features

- Adds an "Open with VS Code" entry for:
  - **Files**: Open individual files in VS Code.
  - **Folders**: Open entire directories in VS Code.
- Automatically sets the correct command and icon for Visual Studio Code.
- Simple and easy to use.

## Prerequisites

- **Operating System**: Windows
- **Python**: Installed on your system
- **Administrator Privileges**: Required to modify the Windows Registry
- **Visual Studio Code**: Installed at `C:\Program Files\Microsoft VS Code\Code.exe` (or adjust the path in the script).

## Usage

1. Clone this repository or download the script file.
2. Open a terminal with administrator privileges.
3. Run the script:
   ```bash
   python add_open_with_vscode.py
