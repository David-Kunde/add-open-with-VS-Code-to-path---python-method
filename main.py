import os
import winreg

def add_open_with_vscode():
    """
    Adds 'Open with VS Code' to the right-click menu for files and folders.
    """

    # Path to VS Code executable --replace with your vc code exe file path
    vscode_path = r'"C:\Program Files\Microsoft VS Code\Code.exe"'

    # Registry keys to modify
    context_menu_keys = {
        "Files": r"*\\shell\\Open with VS Code",
        "Folders": r"Directory\\shell\\Open with VS Code"
    }

    try:
        for key_type, reg_path in context_menu_keys.items():
            # Create the base registry key
            with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, reg_path) as key:
                winreg.SetValue(key, '', winreg.REG_SZ, "Open with VS Code")
                winreg.SetValueEx(key, "Icon", 0, winreg.REG_SZ, vscode_path)

            # Create the 'command' subkey and set its value
            command_path = os.path.join(reg_path, "command")
            with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, command_path) as cmd_key:
                winreg.SetValue(cmd_key, '', winreg.REG_SZ, f'{vscode_path} "%1"')

        print("'Open with VS Code' has been added to the context menu for files and folders.")
    except PermissionError:
        print("Permission denied. Please run this script as an administrator.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    add_open_with_vscode()
