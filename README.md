# Flask Video Streaming

Real-time video streaming application based on Flask, designed for Raspberry Pi with camera module support.

## Features

- Real-time video streaming
- Raspberry Pi camera module integration  
- Lightweight web interface
- Multi-client support

## Hardware Requirements

- Raspberry Pi (suggest Pi 4/5)
- Raspberry Pi Camera Module

## Software Dependencies

- Python 3.x
- Flask
- picamera
- OpenCV

## Quick Start

1. Clone the repository
```shell
git clone https://github.com/Dion4cen/flask-video-streaming.git
```


2. Install dependencies
Make the install script executable and run it
```shell
chmod +x install_requirements.sh
./install_requirements.sh
```

3. Run the application
```shell
python app.py
```

4. Access
Open your browser and navigate to `http://your-raspberry-pi-ip:5000`

## Project Structure

    flask-video-streaming/
    ├── app.py              # Main application
    ├── camera.py           # Camera module
    ├── templates/          # HTML templates
    └── static/            # Static assets

## Usage Guide

1. Ensure Raspberry Pi camera is properly connected and enabled
2. After running the app, view the live stream through web interface
3. Accessible from any device on the local network


