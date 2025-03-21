# Realtek Audio PM Switch

![GitHub tag (latest SemVer pre-release)](https://img.shields.io/github/v/tag/ConceptExplorer/Realtek-Audio-PM-Switch?include_prereleases&label=version)

A simple GUI application to **fix the Realtek audio popping issue** by toggling power management settings for Realtek audio devices on Windows.*
  
  *Hopefully this workaround fixes your Realtek audio device until they fix it in the driver.

![Realtek Audio PM Switch](Realtek-Audio-PM-Switch_v0.1.0.png)

## Description

This application allows users to enable or disable power management for Realtek audio devices by modifying the Windows registry.

## Version

Current pre-release version: **v0.1.0**

## Requirements

- Python 3.6 or higher
- `tkinter` (usually included with Python)
- `pywin32` library

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/ConceptExplorer/Realtek-Audio-PM-Switch.git
   cd Realtek-Audio-PM-Switch

Requirements:
Install the pywin32 library:
pip install pywin32

## Usage

### Running the Script

Run the script with administrative privileges:

```sh
python realtek_audio_pm_switch.py

Run the EXE file by double-clicking it or running it from the command prompt:
dist\realtek_audio_pm_switch.exe

License
This project is licensed under the MIT License.

Disclaimer of Warranty and Limitation of Liability: "This software is provided 'as is,' without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, or noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software."

