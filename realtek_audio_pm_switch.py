import os
import sys
import tkinter as tk
from tkinter import messagebox
import winreg
import ctypes

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

def set_cs_enabled(value):
    reg_path = r"SYSTEM\CurrentControlSet\Control\Power"
    reg_name = "CsEnabled"
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_ALL_ACCESS) as reg_key:
            winreg.SetValueEx(reg_key, reg_name, 0, winreg.REG_DWORD, value)
            status = "enabled" if value == 1 else "disabled"
            messagebox.showinfo("Success", f"Power management for Realtek audio is now {status}. (CsEnabled is set to {value})")
    except PermissionError:
        messagebox.showerror("Error", "Permission denied. Please run the script as an administrator.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def create_gui():
    root = tk.Tk()
    root.title("Realtek Audio PM Switch")
    root.geometry("300x150")  # Set the window size

    tk.Label(root, text="Control Power Management:").pack(pady=10)

    def enable_pm():
        set_cs_enabled(1)

    def disable_pm():
        set_cs_enabled(0)

    enable_button = tk.Button(root, text="Power Management On", command=enable_pm, width=20)
    enable_button.pack(pady=5)

    disable_button = tk.Button(root, text="Power Management Off", command=disable_pm, width=20)
    disable_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    if not is_admin():
        request_admin()
        sys.exit(0)
    create_gui()
