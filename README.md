# capstoneProject
Repository for ECE443 Capstone Project 

## Overview
This project is a Python-based robotic system designed to drive down a sidewalk using a depth camera, lidar, GPS, IMU, encoders, and bump sensors. The project consists of multiple Python scripts that communicate using the PyPubSub library, each responsible for a specific task within the system. A Bash script is also included to run all the Python scripts simultaneously.

## Installation
1. Install Python 3.7 or later from https://www.python.org/downloads/ or using your package manager.
2. Clone the repository or download the project files to your local machine.
3. In your terminal, navigate to the project folder.
4. Install the required Python packages with the following command:
```bash
pip install -r requirements.txt
```

## Usage
1. Make the "start.sh" script executable by running the following command in your terminal:
```bash
chmod +x start.sh
```
2. Run the "start.sh" script to start all the Python scripts simultaneously:
```bash
./start.sh
```

 <br>

# capstoneProject

## vision_system.py
**Description:** Processes depth camera data to detect the edges of the sidewalk and adjusts the steering to keep the robot centered on the sidewalk.

**Inputs:** Depth camera data.

**Outputs:** Steering offset.

<br>

## path_finding.py
**Description:** Processes lidar data and uses Dijkstra's algorithm to plan a path from the robot's current GPS coordinates to the desired GPS endpoint.

**Inputs:** Lidar data, current GPS coordinates, desired GPS endpoint.

**Outputs:** Pathfinding vector.

 <br>

## esp32_driver.py
**Description:** Communicates with a custom ESP32 board using a custom serial command interface to retrieve IMU, GPS, and bump stop data from the ESP32's peripherals. Subscribes to an unlock topic to control the package lock box on the robot.

**Inputs:** Serial data from ESP32, unlock topic.

**Outputs:** IMU data, GPS data, bump stop data.

 <br>

## emergency_stop.py
**Description:** Monitors bump stop, control, and safety topics to determine if the robot should stop driving due to an emergency condition.

**Inputs:** Bump stop data, control data, safety data.

**Outputs:** Stop topic.

 <br>

## drive_fusion.py
**Description:** Processes data from the pathfinding and vision systems to determine the robot's drive direction and steering offset. Monitors the stop topic to halt driving when necessary.

**Inputs:** Pathfinding vector, steering offset, stop topic.

**Outputs:** Left/ right motor throttle.

 <br>

## motor_driver.py
**Description:** Controls the left and right motor speeds based on drive fusion data. Communicates with a SmartDriveDuo motor controller using its packetized serial protocol.

**Inputs:** Left/ right motor throttle.

**Outputs:** Motor control commands.

 <br>

## user_gui.py
**Description:** Hosts a web interface for user control of the robot. The robot connects to a hotspot on a laptop, and the user can access the web interface at a specific IP address. The web interface provides controls for stopping, starting, and selecting an endpoint for the robot. This script also communicates with the necessary topics.

**Inputs:** User commands from the web interface.

**Outputs:** Control commands to various topics.