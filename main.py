import serial
import time
import keyboard

# IMPORTANT: Replace 'COM3' with the correct port for your micro:bit.
# - Windows: 'COMx' (e.g., 'COM3')
# - macOS: '/dev/cu.usbmodemxxxxx'
# - Linux: '/dev/ttyACMx'
MICROBIT_PORT = 'COM3' 
BAUD_RATE = 115200

def run_keyboard_simulation():
    """
    Connects to the micro:bit and simulates key presses based on button input.
    """
    print("Attempting to connect to micro:bit...")
    try:
        # Establish a serial connection with the micro:bit
        ser = serial.Serial(MICROBIT_PORT, BAUD_RATE, timeout=1)
        print(f"Successfully connected to micro:bit on {MICROBIT_PORT}")
        print("Press button A on the micro:bit for 'Enter'")
        print("Press button B on the micro:bit for 'Backspace'")
        print("Press Ctrl+C in this terminal to quit.")

        while True:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()

            if line: # If a line was received
                print(f"Received from micro:bit: '{line}'") # Optional: for debugging
                
                if line == "A":
                    print("Simulating 'Enter' key press...")
                    keyboard.press_and_release('enter')
                
                elif line == "B":
                    print("Simulating 'Backspace' key press...")
                    keyboard.press_and_release('backspace')

    except serial.SerialException:
        print(f"Error: Could not find the micro:bit on port {MICROBIT_PORT}.")
        print("Please check the port name and ensure the micro:bit is connected.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Program terminated.")

if __name__ == "__main__":
    # A small delay to give you time to switch to another window
    print("Starting in 3 seconds...")
    time.sleep(3)
    run_keyboard_simulation()