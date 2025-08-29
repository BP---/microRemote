import serial
import time
import keyboard
import argparse

# IMPORTANT: Replace 'COM3' with the correct port for your micro:bit.
# - Windows: 'COMx' (e.g., 'COM3')
# - macOS: '/dev/cu.usbmodemxxxxx'
# - Linux: '/dev/ttyACMx'
DEFAULT_MICROBIT_PORT = 'COM3'
BAUD_RATE = 115200

def run_keyboard_simulation(port: str):
    """
    Connects to the micro:bit and simulates key presses based on button input.
    """
    print(f"Attempting to connect to micro:bit on port {port}...")
    try:
        # Establish a serial connection with the micro:bit
        ser = serial.Serial(port, BAUD_RATE, timeout=1)
        print(f"Successfully connected to micro:bit on {port}")
        print("Press button A on the micro:bit for 'Enter'")
        print("Press button B on the micro:bit for 'Backspace'")
        print("Press Ctrl+C in this terminal to quit.")

        while True:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()

            if line: # If a line was received
                print(f"Received from micro:bit: '{line}'") # Optional: for debugging
                
                if line == "A":
                    print("swapping...")
                    keyboard.press_and_release('k')

                    keyboard.press_and_release('ctrl+tab')
                    keyboard.press_and_release('win+d')
                
                elif line == "B":
                    print("going back...")

                    keyboard.press_and_release('alt+tab')
                    time.sleep(0.2)
                    keyboard.press_and_release('ctrl+shift+tab')
                    keyboard.press_and_release('k')

                    
                    

    except serial.SerialException:
        print(f"Error: Could not find the micro:bit on port {port}.")
        print("Please check the port name and ensure the micro:bit is connected.")
    except KeyboardInterrupt:
        print("\nInterrupted by user (Ctrl+C). Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Program terminated.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="micro:bit remote keyboard bridge")
    parser.add_argument("--port", "-p", default=DEFAULT_MICROBIT_PORT,
                        help=f"Serial port for micro:bit (default: {DEFAULT_MICROBIT_PORT})")
    args = parser.parse_args()

    # A small delay to give you time to switch to another window
    print("Starting in 1 seconds...")
    time.sleep(1)
    run_keyboard_simulation(args.port)