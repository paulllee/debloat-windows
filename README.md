# Welcome to Debloating Windows

This script automates the uninstallation of 45+ Windows (and HP) applications that are installed onto your PC by default.

It will also handle the Registries for Xbox Game Bar and OneDrive

# Prerequisites 

- Install **App Installer** from Microsoft Store

- Install **Python 3.10+** from the [Python Website](https://www.python.org/downloads/)

# Installation

Open the Terminal as Administrator and run `py main.py` in the same local directory.

# Post Installation

After the script is complete, make sure to follow the instructions on the Terminal. First reboot your device the move all the files from the `C:/Users/%USERPROFILE%/OneDrive` to `C:/Users/%USERPROFILE%/`.

After moving all the files, uninstall any remaining bloat shortcuts in the Start Menu (they aren't actually installed onto the device, they are just shortcuts from Windows/HP).
