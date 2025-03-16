# Virtual-Piano

## Overview
A virtual paino built using IoT andAI technology, powered by a Raspberry Pi4. The system utilises a camera to detect finger placement, offers real-time feedback, and allows multi-user access through mobile devices. The project integrates sensors, cloud connectivity, and date visualisation to create an engaging learning experience.

---

## Key Features
- **Real-Time Finger Detection**: Uses a camera and AI to detect and map finger positions.
- **Multi-User Access**: Mobile phones connect via Bluetooth or Wi-Fi, enabling multiple users.
- **Interactive Feedback**: Visual, audio, or LED-based cues for correct or incorrect notes.
- **IoT Integration**: Cloud-based data storage and anlysis using Azure IoT Hub.
- **Data Visualisation**: Displays user performance etrics on an LCD screen or mobile app.

---

## Hardware Components
- **Raspberry Pi 4 (Core Processor)**
- **Camera Module for finger placement detection**
- **LCD Display for note visualisation and instructions**
- **PIR Motion Sensor for etecting user presence** (optional)
- **Ultasonic Ranger for keyboard calibration** (optional)
- **LEDs for interactive bisual feedback**
- **Bluetooth/Wi-Fi for multi-device connectivity**

---

## Software and Tools
-**Python**: Programming language for development.
-**OpenCV**: For real-time finger detection and image processing.
-**TensorFlow/TensorFlow Lite**: Optional for training and deploying AI models.
-**Azure IoT Hub**: For cloud integration and data analysis.
-**MQTT**: For secure and lightweight data communication.
-**Blynk**: Mobile App for real-time visualisation and control.
-**Custom Vision AI**: For recognising and mapping finger positions.
-**Docker (Optional)**: For containerising and simplifying deployments.

---

## Setup Instrutions

## Hardware Setup
1. Connect the camera module to the Raspberry Pi.
2. Attach the LCD display and any additional sensors (e.g., LEDs, PIR sensor.)

### Install Dependencies
Run the following commands to set up your environment:
```bash
sudo apt-get update
sudo apt-get install python3-pip
pip3 install opencv-python tensorflow azure-iot-device paho-mqtt blynklib
```
### Run Command
```bash
python3 virtual_piano.py
```

