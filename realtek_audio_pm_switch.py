import os
import sys
import tkinter as tk
from tkinter import messagebox
import winreg
import ctypes  # Make sure to import ctypes

def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

def request_admin():
    if sys.version_info[:2] < (3, 5):
        raise RuntimeError("This script requires at least Python 3.5")
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)

def toggle_cs_enabled():
    reg_path = r"SYSTEM\CurrentControlSet\Control\Power"
    reg_name = "CsEnabled"
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_ALL_ACCESS) as reg_key:
            current_value, reg_type = winreg.QueryValueEx(reg_key, reg_name)
            new_value = 0 if current_value == 1 else 1
            winreg.SetValueEx(reg_key, reg_name, 0, winreg.REG_DWORD, new_value)
            status = "disabled" if new_value == 0 else "enabled"
            messagebox.showinfo("Success", f"Power management for Realtek audio is now {status}. (CsEnabled is set to {new_value})")
    except FileNotFoundError:
        with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as reg_key:
            winreg.SetValueEx(reg_key, reg_name, 0, winreg.REG_DWORD, 1)
            messagebox.showinfo("Success", "Power management for Realtek audio was created and enabled. (CsEnabled is set to 1)")
    except PermissionError:
        messagebox.showerror("Error", "Permission denied. Please run the script as an administrator.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def create_gui():
    root = tk.Tk()
    root.title("Toggle Realtek Power Management")

    toggle_button = tk.Button(root, text="Toggle Power Management", command=toggle_cs_enabled)
    toggle_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    if not is_admin():
        request_admin()
        sys.exit(0)
    create_gui()
