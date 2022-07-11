# Welcome to Debloating Windows

This Python script automates the uninstallation of 45+ Windows (and HP) applications that are installed onto your PC by default. 

It will also handle the Registries for Xbox Game Bar and OneDrive.

*Edge* is not included because of Windows 11's strict file extensions that only work with Edge.

# Prerequisites 

- Install **App Installer** from Microsoft Store

- Install **Python 3.10.x** from the [Python Website](https://www.python.org/downloads/)

# Installation

Download the [Latest Release](https://github.com/paulllee/debloat-windows/releases)

# Instructions

Right click the `debloat-windows.exe` file and click **Run as Administrator**. Then follow the instructions provided in the terminal.

# Post Installation

After the script is complete, make sure to follow the instructions on the Terminal. First reboot your device the move all the files from the `C:/Users/%USERPROFILE%/OneDrive` to `C:/Users/%USERPROFILE%/`.

After moving all the files, uninstall any remaining bloat shortcuts in the Start Menu (they aren't actually installed onto the device, they are just shortcuts from Windows/HP).

# License

Distributed under the GNU General Public License v3.0. See [LICENSE](/LICENSE/) for more information.
