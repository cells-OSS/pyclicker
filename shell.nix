{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python313
    python313Packages.pynput
    python313Packages.pyqt6
  ];

  shellHook = ''
    echo "PyClicker development environment loaded"
  '';
}
