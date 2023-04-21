from pubsub import pub

def calculate_motor_speeds(pathfinding_vector, steering_offset):
    x, y = pathfinding_vector

    # Calculate the base speed for each motor
    left_base_speed = y + x
    right_base_speed = y - x

    # Apply the steering offset
    left_motor_speed = left_base_speed + steering_offset
    right_motor_speed = right_base_speed - steering_offset

    # Normalize motor speeds to a range of 0 to 1
    max_speed = max(abs(left_motor_speed), abs(right_motor_speed))
    if max_speed > 1:
        left_motor_speed /= max_speed
        right_motor_speed /= max_speed

    return left_motor_speed, right_motor_speed

def process_drive_data(pathfinding_vector, steering_offset, stop):
    if stop:
        # If the stop topic is True, set motor speeds to 0
        left_motor_speed = 0
        right_motor_speed = 0
    else:
        # Calculate the motor speeds based on pathfinding vector and steering offset
        left_motor_speed, right_motor_speed = calculate_motor_speeds(pathfinding_vector, steering_offset)

    # Publish motor speeds to the motor control topic
    pub.sendMessage('motor_control_data', motor_data=(left_motor_speed, right_motor_speed))

def main():
    # Subscribe to the relevant topics
    pub.subscribe(lambda pathfinding_vector: process_drive_data(pathfinding_vector=pathfinding_vector, steering_offset=None, stop=None), 'pathfinding_data')
    pub.subscribe(lambda steering_offset: process_drive_data(pathfinding_vector=None, steering_offset=steering_offset, stop=None), 'steering_data')
    pub.subscribe(lambda stop: process_drive_data(pathfinding_vector=None, steering_offset=None, stop=stop), 'stop_data')

    # Main loop
    while True:
        pass

if __name__ == "__main__":
    main()
