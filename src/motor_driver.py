import serial
from pubsub import pub

# Replace '/dev/ttyUSB0' with the correct serial port for your setup
SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

# Initialize the serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

def send_motor_command(left_throttle, right_throttle):
    # Convert throttle percentages to motor controller values
    left_value = int(63 + (left_throttle * 192))
    right_value = int(63 + (right_throttle * 192))

    # Create a packet to send to the motor controller
    packet = bytearray([0x80, 0x00, left_value, right_value, 0x00])

    # Compute the checksum
    checksum = (sum(packet[1:]) % 256)
    packet[-1] = checksum

    # Send the packet to the motor controller
    ser.write(packet)

def control_motors(motor_data):
    # Extract left and right motor throttle percentages from the data
    left_throttle, right_throttle = motor_data

    # Send motor commands
    send_motor_command(left_throttle, right_throttle)

def main():
    # Subscribe to the motor control topic
    pub.subscribe(control_motors, 'motor_control_data')

    # Main loop
    while True:
        pass

if __name__ == "__main__":
    main()
