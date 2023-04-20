#!/bin/bash
python3 src/vision_system.py &
python3 src/path_finding.py &
python3 src/esp32_driver.py &
python3 src/emergency_stop.py &
python3 src/drive_fusion.py &
python3 src/motor_driver.py &
python3 src/user_gui.py
