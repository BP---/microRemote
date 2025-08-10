microRemote
===========

Simple Python tool that listens to a BBC micro:bit over a serial connection and simulates keyboard key presses on your computer:

Button mappings:

- A -> Enter
- B -> Backspace

Requirements
------------
- Python 3.11+
- micro:bit flashed with a program that prints either `A` or `B` over serial when buttons are pressed.

Install dependencies (project uses uv / PEP 621):

```
uv sync
```

Run
---

Default (assumes micro:bit is on COM3):

```
uv run main.py
```

Specify a different serial port:

```
uv run main.py --port COM6
```

or short form:

```
uv run main.py -p /dev/cu.usbmodem1101
```

Press Ctrl+C to exit.

Troubleshooting
---------------
If you see an error that the port cannot be opened:
1. Confirm the correct port (Windows Device Manager, `mode` command, or on macOS/Linux list with `ls /dev/tty.*` or `ls /dev/ttyACM*`).
2. Ensure no other program (e.g., a serial monitor) is using the port.
3. Replug the micro:bit and retry.

License
-------
MIT
