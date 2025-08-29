microRemote
===========

Simple Python tool that listens to a BBC micro:bit over a serial connection.
There are different files for different use cases. The main functionality is that one Micro:bit sends either "A" or "B" over serial. This is usually initiated by a different Micro:bit that sends a message over radio, to the Micro:bit connected to the computer. 



Requirements
------------
- Python 3.11+
- micro:bit flashed with a program that prints either `A` or `B` over serial when buttons are pressed (or a different event).

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
