# LyL.gg on Linux

To use any scripts in here, put your details inside the `config.py` file.

Run the scripts via
`python $script`,
e.g. `python insert.py`

Purposes:
- insert.py: Insert the steam ID at a place where the Lyl Launcher can read it and use it for its bonus program
- run_arma3.py: Run Arma 3 and connect to LyL Altis Life. You may connect via the Arma 3 Launcher or anything.
- run_lyl.py: Run the LyL launcher.

## Dependencies

- You need protontricks, either native or flatpak. I had bugs with the native package and chose Flatpak. Make sure your protontricks flatpak can access the directory your `lyl-launcher.exe` is located at!!
- Python.
- VDF for Python. For Arch, there is an AUR package called `python-vdf`.
- The LyL launcher. Put the executable in this repository or edit the path to it in `config.py`.

## Disclaimer

No guarantees any scripts work and are free of bugs.

