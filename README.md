# pyclicker
A simple clicker app designed to be used for automation.

# PREREQUISITES
[Python](https://www.python.org/)

# INSTALLATION INSTRUCTIONS

**For Windows**
Ensure you have [Python](https://www.python.org/) installed and simply run the script.

**For MacOS, Linux**
Simply run the python script using the python3 command.

**For NixOS**
Since NixOS uses a declarative approach, you will need to edit your configuration.nix file located at "/etc/nixos".
Once you're in, add the following to entries into your package list:

packages = with pkgs; [
    python313Packages.pynput
    python313Packages.pyqt6
];

Once done, save and quit the file and rebuild your system (sudo nixos-rebuild switch)

You can now run the python file using the python3 command.